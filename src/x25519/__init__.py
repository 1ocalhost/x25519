from . import djbec

SCALAR_SIZE = POINT_SIZE = 32
BASE_POINT = djbec.encodeint(9)


def clamp(n):
    n = bytearray(n)
    n[0] &= 248
    n[31] = (n[31] & 127) | 64
    return n if djbec.PY3 else str(n)


def curve25519(n, p):
    assert isinstance(n, bytes) and len(n) == SCALAR_SIZE
    assert isinstance(p, bytes) and len(p) == POINT_SIZE
    n = clamp(n)

    def curve25519_impl(x):
        return djbec.curve25519(x, djbec.decodeint(p))

    for fn in (
        djbec.decodeint,
        curve25519_impl,
        djbec.encodeint,
    ):
        n = fn(n)

    return n


def scalar_mult(scalar, point):
    return curve25519(scalar, point)


def scalar_base_mult(scalar):
    return curve25519(scalar, BASE_POINT)
