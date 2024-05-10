from flask import Flask, request, jsonify
from app.emoji_encoder_decoder import EmojiEncoderDecoder
from flask_cors import CORS

app = Flask(__name__)
encoder_decoder = EmojiEncoderDecoder()

CORS(app)


@app.route("/encode", methods=["POST"])
def encode_text():
    data = request.json
    text = data["text"]
    encoded_text = encoder_decoder.encode(text)
    return jsonify({"encoded_text": encoded_text})


@app.route("/decode", methods=["POST"])
def decode_text():
    data = request.json
    text = data["text"]
    decoded_text = encoder_decoder.decode(text)
    return jsonify({"decoded_text": decoded_text})


if __name__ == "__main__":
    app.run()
