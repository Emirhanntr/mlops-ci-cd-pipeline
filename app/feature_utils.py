import hashlib


def hashed_feature(text: str, num_buckets: int = 1024) -> int:
    """
    Deterministic hashing -> bucket index
    (Unit test bunun doğruluğunu kontrol edecek)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if num_buckets <= 0:
        raise ValueError("num_buckets must be > 0")

    h = hashlib.md5(text.encode("utf-8")).hexdigest()
    return int(h, 16) % num_buckets
