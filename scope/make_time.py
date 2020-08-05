import time
def make_timer():
    ultima_chamada = None

    def elapsed():
        nonlocal ultima_chamada
        now = time.time()
        if ultima_chamada is None:
            ultima_chamada = now
            return None
        result = now - ultima_chamada
        ultima_chamada = now
        return result

    return elapsed

