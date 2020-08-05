from .rotate_list import rotate_list
import pytest

l = [1,2,3,4]
@pytest.mark.parametrize ('r1, l',
                         [
                             (rotate_list(l), [1,2,3,4])
                         ]    
                        )
def test_rotate_list(r1, l):
    assert r1 != l





