def count_vowel_consonant_pairs(text):
    """
    Counts the number of occurrences where a vowel is
    immediately followed by a consonant in the input string.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: Count of vowel-consonant pairs.
    """
    if not isinstance(text, str):  # Explicitly check input type
        raise TypeError("Input must be a string")

    vowels = "aeiouAEIOU"
    count = 0

    for i in range(len(text) - 1):
        if text[i] in vowels and text[i + 1].isalpha() and text[i + 1] not in vowels:
            count += 1

    return count

