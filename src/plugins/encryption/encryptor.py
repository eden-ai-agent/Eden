"""Very small symmetric XOR based encryption utilities."""


def encrypt(data: str, key: int) -> str:
    """Encrypt ``data`` with a simple XOR cipher."""

    return "".join(chr(ord(c) ^ key) for c in data)


def decrypt(data: str, key: int) -> str:
    """Decrypt XOR encrypted ``data``."""

    return encrypt(data, key)

