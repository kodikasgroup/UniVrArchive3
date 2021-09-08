import hashlib
import pprint


class HashHandler:
    lookup_table = {}
    instances_table = {}

    @classmethod
    def generate_hash(cls, text):
        result = hashlib.md5(text.encode()).hexdigest()
        cls.lookup_table[result] = text
        cls.instances_table[result] = cls.instances_table.get(result, 0) + 1
        return result

    @classmethod
    def get_corresponding_text(cls, hash_text):
        # pprint.pprint(cls.lookup_table)
        result = cls.lookup_table[hash_text]
        cls.instances_table[hash_text] = cls.instances_table[hash_text] - 1
        if cls.instances_table[hash_text] == 0:
            cls._delete_occurrence(hash_text)

        return result

    @classmethod
    def _delete_occurrence(cls, hash_text):
        del cls.instances_table[hash_text]
        del cls.lookup_table[hash_text]
