"""PR08 Filter tests."""
import filter
import random

def test_remove_vowels_when_no_vowels():
    """Test when no vowels in remove_vowels."""
    assert filter.remove_vowels("QqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm") == "QqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"


def test_remove_vowels_only_vowels_longer():
    """Test when only vowels in remove_vowels."""
    string = random.choices("aeiouAEIOU", k=10)
    string = "".join(string)
    assert filter.remove_vowels(string) == ""


def test_remove_vowels_one_vowel():
    """Test when only one vowel in remove_vowels."""
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for letter in vowels:
        assert filter.remove_vowels(letter) == ""


def test_remove_vowels_empty_string():
    """Test when string is empty in remove_vowels."""
    assert filter.remove_vowels("") == ""


def test_longest_filtered_word_empty_returns_none():
    """Test when list is empty in longest_filtered_word."""
    assert filter.longest_filtered_word([]) is None


def test_longest_filtered_word_vowels_in_strings():
    """Test when only vowels in list in longest_filtered_word."""
    list_a = []
    for _ in range(0, 10):
        temp = random.choices("aeiouAEIOU", k=10)
        b = "".join(temp)
        list_a.append(b)
    assert filter.longest_filtered_word(list_a) == ""


def test_longest_filtered_word_no_vowels_in_strings():
    """Test when no vowels in list in longest_filtered_word."""
    list_a = []
    for _ in range(0, 10):
        temp = random.choices("qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM", k=10)
        b = "".join(temp)
        list_a.append(b)
    assert filter.longest_filtered_word(list_a) == list_a[0]


def test_longest_filtered_word_empty_string():
    """Test when only empty string in longest_filtered_word."""
    assert filter.longest_filtered_word([""]) == ""


def test_longest_filtered_word_find_longest_before_filtering():
    """Test if find longest word before filtering."""
    list_a = []
    for _ in range(10):
        temp = random.choices("qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNMaeiouAEIOU", k=random.randrange(5, 10))
        b = "".join(temp)
        list_a.append(b)
    i = 0
    while i < len(list_a):
        list_a[i] = filter.remove_vowels(list_a[i])
        i += 1
    list_a.sort(key=len, reverse=True)
    assert filter.longest_filtered_word(list_a) == list_a[0]


def test_sort_list_empty_list():
    """Test when list empty in sort_list."""
    assert filter.sort_list([]) == []


def test_sort_list_list_len_1():
    """Test when length of list is 1 in sort_list."""
    list_a = random.choices("qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNMaeiouAEIOU", k=10)
    string_a = "".join(list_a)
    list_a = [string_a]
    list_b = [None]
    list_b[0] = filter.remove_vowels(list_a[0])
    assert filter.sort_list(list_a) == list_b