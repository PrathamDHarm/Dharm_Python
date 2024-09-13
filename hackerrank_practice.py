def count_vowel_substrings(s):
    vowels = 'aeiouAEIOU'  # List of vowels (upper and lowercase)
    total_points = 0
    
    # Iterate over the string
    for i in range(len(s)):
        if s[i] in vowels:  # Check if the character is a vowel
            # Substrings starting from this vowel are s[i:] (from i to end)
            total_points += len(s) - i  # Count all substrings starting from this vowel

    return total_points

# Example usage
string = "BANANA"
kevin_points = count_vowel_substrings(string)
print(f"Kevin's points: {kevin_points}")
