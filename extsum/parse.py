import itertools as it
from typing import Iterator, Optional

START_PICSUM_TAG = 230
END_PICSUM_TAG = 240
PICSUM_TAG = b'Picsum ID:'


class Parse:
    def __init__(self, byte_stream: Iterator):
        """Representation of a photo as a byte stream

        :param byte_stream: the photo byte stream
        """

        self.byte_stream: Iterator = byte_stream
        self._tag_verified: bool = self._verify_tag()

    def _verify_tag(self) -> bool:
        """Returns true if `Picsum ID:` tag is found

        Note that `tee()` is not thread safe. However, the body of this method
        will always be executed in a single thread
        """

        tag_found = it.islice(self.byte_stream,
                              START_PICSUM_TAG,
                              END_PICSUM_TAG)
        tag_expected = (b'%c' % byte for byte in PICSUM_TAG)
        check_gen = (f == e for f, e in it.zip_longest(tag_found, tag_expected))

        iter_all, iter_any = it.tee(check_gen, 2)
        tag_verified = all(iter_all) and any(iter_any)

        return tag_verified

    def find_id(self) -> Optional[str]:
        """Returns the ID if the correct tag is detected

        * In case a non-UTF-8 character is encountered, it will be replaced by
          the 'replacement character' FFFD.

        * In UTF-8, 0xFF is forbidden and we are actually looping until we
          find FFDB which denotes a quantization table in Exif
          (https://www.exif.org/Exif2-2.PDF).

        * This method assumes that once the `PICSUM_TAG` has been detected,
          the object is a valid Picsum photo and hence Exif encoded
        """

        if self._tag_verified:
            # First character after PICSUM_TAG is always a space
            id_slice = it.islice(self.byte_stream, END_PICSUM_TAG + 1, None)
            id_found = ''
            for byte in id_slice:
                if byte != b'\xff':
                    id_found += byte.decode('utf-8', 'replace')
                else:
                    break
            return id_found
        else:
            return None
