class BitArray(object):
    """
    A simple implementation of an array of bits, accessable using the regular
    item access syntax.
    """

    def __init__(self, length, default=False):
        self.length = length
        byte_length = (length // 8) + 1

        if default:
            self.data = bytearray([255] * byte_length)
        else:
            self.data = bytearray(byte_length)

    def __getitem__(self, key):
        return bool((self.data[key // 8] >> (key % 8)) & 1)

    def __setitem__(self, key, value):
        raw = self.data[key // 8]
        set_val = bool(value) << (key % 8)

        mask = ~(1 << (key % 8))
        updated = (raw & mask) | set_val

        self.data[key // 8] = updated

    def __len__(self):
        return self.length

    def __iter__(self):
        for b in self.data:
            for i in range(8):
                yield bool((1 << i) & b)

    def __repr__(self):
        return self.data.hex()
