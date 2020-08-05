from .scoping import Scope


def test_scope():
    t1 = Scope()
    message = 'global'
    assert message == 'global'
    assert t1.message == 'global'
    t1.func()
    assert t1.message == 'func'
    

