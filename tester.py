"""Here are the unit tests that must be verified by the implementation.

@see: this_is_where_you_code.ThisIsWhereYouCode
@author: ataillefer@nuxeo.com
"""

import unittest
from this_is_where_you_code import ThisIsWhereYouCode


class Tester(unittest.TestCase):

    def setUp(self):
        self.impl = ThisIsWhereYouCode()

    def test_extensions(self):
        inputs = ['somefile.dat', 'movie.torrent', 'noextension', '.htaccess', 'noext.', None]
        expected = ['dat', 'torrent', None, 'htaccess', '', None]

        for i in range(len(inputs)):
            self.assertEqual(self.impl.get_file_name_extension(inputs[i]), expected[i])

    def test_longest_string(self):
        inputs = [['a', 'ab', 'abc'],
                  ['abc', 'ab', 'a'],
                  ['big', ['ab', 'a', ], 'tiny'],
                  ['big', ['ab', 'a', ['superbig', 'a']], 'tiny'],
                  [123, 23123123, 'a'],
                  [None, [], 'a']]
        expected = ['abc', 'abc', 'tiny', 'superbig', 'a', 'a']

        for i in range(len(inputs)):
            self.assertEqual(self.impl.get_longest_string(inputs[i]), expected[i])

    def test_array_equals(self):
        self.assertTrue(self.impl.are_arrays_equal([], []))
        self.assertTrue(self.impl.are_arrays_equal(['a', 'b', 'c'], ['a', 'b', 'c']))
        self.assertFalse(self.impl.are_arrays_equal(['a', 'b', 'c'], ['b', 'a', 'c']))
        self.assertFalse(self.impl.are_arrays_equal(['a', 'b', 'c'], ['ab', '', 'c']))
        self.assertFalse(self.impl.are_arrays_equal(None, []))
        self.assertFalse(self.impl.are_arrays_equal(['a', None, 'b'], ['a', 'b']))
        self.assertFalse(self.impl.are_arrays_equal(None, []))
        self.assertTrue(self.impl.are_arrays_equal(None, None))

    def test_compressor(self):
        inputs = ['abc', 'aaabbc', None, 'abccc', 'aaaaaaaaaaaaaaabb', 'aabbbbaaa']
        expected = ['abc', '3a2bc', None, 'ab3c', '15a2b', '2a4b3a']

        for i in range(len(inputs)):
            self.assertEqual(self.impl.get_compressed_string(inputs[i]), expected[i])

    def test_sorter(self):
        """Please read carefully the doc of ThisIsWhereYouCode.get_sorted_array.

        i.e. the test is not broken.
        """
        inputs = [['a', 'ab', 'abc'],
                  ['abc', 'ab', 'a'],
                  ['abc', 'aab', 'abbb'],
                  ['abc', 'acc', 'ab'],
                  ['aaaa', 'aaab', 'ab']]
        expected = [['a', 'ab', 'abc'],
                    ['a', 'ab', 'abc'],
                    ['aab', 'abbb', 'abc'],
                    ['acc', 'ab', 'abc'],
                    ['aaab', 'aaaa', 'ab']]

        for i in range(len(inputs)):
            self.assertTrue(self.impl.are_arrays_equal(expected[i], self.impl.get_sorted_array(inputs[i])))

if __name__ == '__main__':
    unittest.main()
