def compare_strings(str1, str2):
    differences = []
    len1, len2 = len(str1), len(str2)
    max_len = max(len1, len2)

    for i in range(max_len):
        char1 = str1[i] if i < len1 else ''
        char2 = str2[i] if i < len2 else ''
        if char1 != char2:
            differences.append((char1, char2))

    return differences

def test_compare_strings():
    assert compare_strings("hello", "hallo") == [('e', 'a')]
    assert compare_strings("test", "test") == []
    assert compare_strings("abc", "abcd") == [('', 'd')]
    assert compare_strings("abcd", "abc") == [('d', '')]
    assert compare_strings("", "abc") == [('', 'a'), ('', 'b'), ('', 'c')]
    assert compare_strings("abc", "") == [('a', ''), ('b', ''), ('c', '')]
    assert compare_strings("kitten", "sitting") == [('k', 's'), ('e', 'i'), ('n', 't'), ('', 'g')]

# Example usage:
# We recommend installing an extension to run python tests.
# test_compare_strings()
# print("All tests passed.")
