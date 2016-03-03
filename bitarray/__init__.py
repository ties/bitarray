"""
BitArray class
<https://github.com/ties/bitarray>
"""


class BitArray(object):
    # pylint: disable=too-few-public-methods
    """A simple implementation of an array of bits, accessable using the
    regular item access syntax.
    """
    __slots__ = ('length', 'data')

    def __init__(self, length: int, default: bool=False):
        """Initialise a BitArray with a given length and default values

        Args:
          length: (minimum) length of the array
          default: the value bits should be initialised to
        """
        self.length = length
        byte_length = (length // 8) + 1

        if default:
            self.data = bytearray([255] * byte_length)
        else:
            self.data = bytearray(byte_length)

    def __getitem__(self, key: int) -> bool:
        return bool((self.data[key // 8] >> (key % 8)) & 1)

    def __setitem__(self, key: int, value: bool) -> None:
        raw = self.data[key // 8]
        set_val = bool(value) << (key % 8)

        mask = ~(1 << (key % 8))
        updated = (raw & mask) | set_val

        self.data[key // 8] = updated

    def __len__(self) -> int:
        return self.length

    def __iter__(self):
        # type: () -> Iterable[int]:
        for idx, byte in enumerate(self.data):
            for i in range(8):
                if (8*idx)+i < self.length:
                    yield bool((1 << i) & byte)

    def __repr__(self):
        return self.data.hex()[0:(self.length // 4) + 1]
