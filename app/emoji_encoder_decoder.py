class EmojiEncoderDecoder:
    def __init__(self):
        self.emoji_dict = {
            ":)": "😊",
            ":(": "😞",
            ";)": "😉",
            ":D": "😄",
            "XD": "😆",
            ":P": "😋",
            "<3": "❤️",
            ":O": "😲",
            ":|": "😐",
            ":/": "😕",
            ":*": "😘",
        }
        self.hash_dict = {}  # Словарь для соответствий текста и ключей

    def encode(self, text):
        # Иначе закодировать текст и сохранить соответствие текста и ключа
        encoded_text = self._encode_text(text)
        # Генерация хеша текста
        text_hash = hash(encoded_text)
        # Если текст уже был закодирован, вернуть его ключ
        if text_hash in self.hash_dict:
            return text_hash
        self.hash_dict[text_hash] = encoded_text
        return text_hash

    def decode(self, text_hash):
        if text_hash not in self.hash_dict:
            return "No such hash"
        # Иначе найти соответствующий текст по ключу
        decoded_text = self.hash_dict[text_hash]
        return decoded_text

    def _encode_text(self, text):
        encoded_text = text
        for key, value in self.emoji_dict.items():
            encoded_text = encoded_text.replace(key, value)
        return encoded_text
