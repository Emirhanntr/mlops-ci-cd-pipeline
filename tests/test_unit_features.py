import pytest
from app.feature_utils import hashed_feature

def test_hashed_feature_known_value():
    assert hashed_feature("user_123", 1024) == hashed_feature("user_123", 1024)

def test_hashed_feature_bucket_range():
    b = hashed_feature("abc", 128)
    assert 0 <= b < 128

def test_hashed_feature_type_check():
    with pytest.raises(TypeError):
        hashed_feature(123, 1024)  # type: ignore

def test_hashed_feature_invalid_buckets():
    with pytest.raises(ValueError):
        hashed_feature("abc", 0)
