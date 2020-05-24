"""Test photo parsing."""

import itertools as it
import unittest as unit
from extsum.parse import Parse, PICSUM_TAG, START_PICSUM_TAG


bs_pre_literal = bytearray(START_PICSUM_TAG)


class TestParse(unit.TestCase):
    """Test methods defined by the `Parse` class.

    Here we choose to store the values of 'prelude' generators in memory as we
    know that they'll always be exhausted and used in multiple methods.
    """
    bs_pre = list(b'%c' % byte for byte in bs_pre_literal)
    bs_pre_id = list(it.chain(bs_pre, (b'%c' % byte for byte in PICSUM_TAG)))

    def test_found_correct_tag(self):
        bs_parsed = Parse(self.bs_pre_id)
        self.assertTrue(bs_parsed._tag_verified)

    def test_found_empty_tag(self):
        bs_parsed = Parse(self.bs_pre)
        self.assertFalse(bs_parsed._tag_verified)

    def test_found_subslice_tag(self):
        bs_tag = (b'%c' % byte for byte in b'Picsum ID')
        bs = it.chain(self.bs_pre, bs_tag)
        bs_parsed = Parse(bs)
        self.assertFalse(bs_parsed._tag_verified)

    def test_found_different_tag(self):
        bs_tag = (b'%c' % byte for byte in b'picsum id:')
        bs = it.chain(self.bs_pre, bs_tag)
        bs_parsed = Parse(bs)
        self.assertFalse(bs_parsed._tag_verified)

    def test_found_42_id(self):
        bs = self.bs_pre_id + [b' ', b'4', b'2', b'\xff']
        bs_parsed = Parse(bs)
        self.assertEqual(bs_parsed.find_id(), '42')

    def test_found_empty_id(self):
        bs = self.bs_pre_id + [b' ', b'\xff']
        bs_parsed = Parse(bs)
        self.assertEqual(bs_parsed.find_id(), '')

    def test_found_none_id(self):
        bs_parsed = Parse(self.bs_pre)
        self.assertIsNone(bs_parsed.find_id())

    def test_found_non_utf8_char_id(self):
        bs = self.bs_pre_id + [b' ', b'\x80', b'2', b'\xff']
        bs_parsed = Parse(bs)
        self.assertEqual(bs_parsed.find_id(), '�2')
