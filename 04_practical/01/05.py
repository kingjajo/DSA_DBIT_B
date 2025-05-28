def counting_character(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage
text = "data structures and algorithms"
frequencies = counting_character(text)
print(frequencies)
