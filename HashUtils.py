import hashlib

class HashUtils:

    @staticmethod
    def hash_sha256_hex(to_hash):
        return HashUtils.hash_sha256(to_hash).hexdigest()

    @staticmethod
    def hash_sha256(to_hash):
        if not isinstance(to_hash, bytes):
            to_hash = str.encode(to_hash)
        return hashlib.sha256(to_hash)