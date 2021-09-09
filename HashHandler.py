import hashlib
import pprint


class HashHandler:
    lookup_table = {}

    @classmethod
    def generate_hash(cls, text):
        """

        :param text:
        :return:
        """
        result = hashlib.md5(text.encode()).hexdigest()
        cls.lookup_table[result] = text
        return result

    @classmethod
    def get_corresponding_text(cls, hash_text):
        """

        :param hash_text:
        :return:
        """
        result = cls.lookup_table.get(hash_text, None)
        return result
