"""This is where you have to code.

See docstrings and associated unit tests in the Tester class to understand
what is expected.

@see: tester.Tester
@author: ataillefer@nuxeo.com
"""
import os
import types
import six

def flatten(array):
    if not array:
        return None

    result = []
    for x in array:
        if isinstance(x, types.ListType):
            l = flatten(x)
            if l:
                result += l
        else:
            result.append(x)
    return result


class ThisIsWhereYouCode():

    def get_file_name_extension(self, filename):
        """Return the file extension (with no period).

        Input will be a string, but it may not have a file extension.

        :return: None if the input is None or has no extension and the extension
        without the period otherwise
        """
        try:
            return os.path.splitext(filename)[1][1:] or None
        except AttributeError:
            return None


    def get_longest_string(self, array):
        """Return the longest string contained in the input array.

        The input array can contain nested arrays.

        :return: None if the input is None and the longest string otherwise
        """
        if array:
            array = filter(
                lambda s: isinstance(s, six.string_types), 
                flatten(array))
            return max(array, key=len) if array else None
        return None



    def are_arrays_equal(self, array1, array2):
        """Return True if both arrays contain the same values in the same order.

        :return: True if both arrays contain the same values in the same order
        and False otherwise
        """
        if array1 is None and array2 is None:
            return True
        if array1 is None and array2 is not None:
            return False
        if array2 is None and array1 is not None:
            return False
        if len(array1) != len(array2):
            return False
        if array1 == [] and array2 == []:
            return True
        for x, y in zip(array1, array2):
            if x != y:
                return False
        return True

    def get_compressed_string(self, input_):
        """Compress the input string with a very dummy algorithm.

        Repeated letters are replaced by {n}{letter} where {n} is the number of
        repetitions and {letter} is the letter.
        n must be greater than 1 (otherwise, simply output the letter).

        :param input_: the input string that can only contain letters
        :return: None if the input is None and the compressed string otherwise
        """
        if not input_:
            return None
        buffer = []
        result = ""
        for letter in input_:
            if letter in buffer:
                buffer.append(letter)
            else:
                if buffer:
                    n = len(buffer)
                    last_letter = buffer[0]
                    result += "%s%s" % (n, last_letter) if n > 1 else last_letter
                    buffer = [letter]
                else:
                    buffer.append(letter)
        if buffer:
            n = len(buffer)
            letter = buffer[0]
            result += "%s%s" % (n, letter) if n > 1 else letter
        return result



    def get_sorted_array(self, array):
        """Sort the input array of strings.

        Sort is based on lexicographic order of the corresponding compressed strings.
        Hint: the expected sorting should use get_compressed_string.

        :return: None if the input is None and the sorted array otherwise
        """
        if not array:
            return None
        return sorted(array, key=self.get_compressed_string)

