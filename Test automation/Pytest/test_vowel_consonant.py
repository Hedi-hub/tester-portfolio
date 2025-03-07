import pytest
from vowel_consonant import count_vowel_consonant_pairs


@pytest.mark.parametrize("test_input,expected", [
    ("hello", 1),        # e → l
    ("banana", 3),       # a → n, a → n, a → n
    ("AEIOUbc", 5),      # A → b, E → b, I → b, O → b, U → b
    ("", 0),             # Empty string
    ("12345", 0),        # No alphabets
    ("PyThOn", 1),       # o → n
    ("a!e@i#o$u%", 0)    # Special characters interrupt pairs
])
def test_count_vowel_consonant_pairs(test_input, expected):
    assert count_vowel_consonant_pairs(test_input) == expected


@pytest.mark.parametrize("edge_input,expected", [
    ("", 0),                 # Empty string
    ("a!e@i#o$u%", 0),       # Special characters only
    ("12345", 0),            # Numbers only
    ("a", 0),                # Single vowel
    ("b", 0),                # Single consonant
    ("a1e2i3o4u", 0)         # Vowel-consonant interrupted by numbers
])
def test_edge_cases(edge_input, expected):
    assert count_vowel_consonant_pairs(edge_input) == expected


@pytest.mark.parametrize("invalid_input", [
    None,               # Passing None
    12345,              # Passing an integer
    ["hello"],          # Passing a list
    {"text": "hi"}      # Passing a dictionary
])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        count_vowel_consonant_pairs(invalid_input)


@pytest.mark.parametrize("test_input,expected", [
    ("a" * 1000 + "b" * 1000, 1),  # 1000 vowels followed by 1000 consonants → Expect 1
    ("ab" * 1000, 1000),           # 1000 alternating vowel-consonant pairs → Expect 1000
])
def test_large_inputs(test_input, expected):
    assert count_vowel_consonant_pairs(test_input) == expected


def test_large_random_string():
    import random
    characters = "aeioubcdfghjklmnpqrstvwxyz!@#$%^&*1234567890"
    large_string = "".join(random.choices(characters, k=10000))
    result = count_vowel_consonant_pairs(large_string)
    assert isinstance(result, int)  # We expect an integer result (valid execution)

