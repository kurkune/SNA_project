import json
import unittest

from app.emoji_encoder_decoder import EmojiEncoderDecoder
from app.server import app


class TestEmojiEncoderDecoder(unittest.TestCase):
    def setUp(self):
        self.encoder_decoder = EmojiEncoderDecoder()

    def test_encode(self):
        text = "Hello :)"
        encoded_hash = self.encoder_decoder.encode(text)
        decoded_text = self.encoder_decoder.decode(encoded_hash)
        self.assertEqual(decoded_text, "Hello 😊")

    def test_decode_invalid(self):
        invalid_hash = 12345
        self.assertEqual(self.encoder_decoder.decode(invalid_hash), "No such hash")


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_encode_endpoint(self):
        response = self.app.post('/encode', data=json.dumps({"text": "Hello :)"}),
                                 content_type='application/json')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('encoded_text', data)
        self.assertTrue(isinstance(data['encoded_text'], int))  # Since it should return a hash

    def test_decode_endpoint(self):
        encode_response = self.app.post('/encode', data=json.dumps({"text": "Hello :)"}),
                                        content_type='application/json')
        encode_data = json.loads(encode_response.data)
        encoded_hash = encode_data['encoded_text']

        decode_response = self.app.post('/decode', data=json.dumps({"text": encoded_hash}),
                                        content_type='application/json')
        decode_data = json.loads(decode_response.data)

        self.assertEqual(decode_response.status_code, 200)
        self.assertIn('decoded_text', decode_data)
        self.assertEqual(decode_data['decoded_text'], 'Hello 😊')

    def test_decode_invalid_hash(self):
        response = self.app.post('/decode', data=json.dumps({"text": 999999}),
                                 content_type='application/json')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['decoded_text'], 'No such hash')
