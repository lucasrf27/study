import traceback
import contextlib
import sys

class ContextManage():


    def __enter__(self):
        print('start')
        return ('rodando')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('Normal exit')
        else:
            print('type = {}, value = {}, tb = {}'.format(exc_type, exc_val, exc_tb))

    @contextlib.contextmanager
    def context_manage():
        print('ENTER')
        try:
            yield 'you are in a with-block'
            print('Normal EXIT')
        except Exception:
            print('EXCEPTION {}'.format(sys.exc_info()))
            



with ContextManage.context_manage() as f:
    raise ValueError('ok')
    print(f)