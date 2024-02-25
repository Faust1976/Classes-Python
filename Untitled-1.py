def find_common_characters(str1, str2):

    str1_lower = str1.lower()
    str2_lower = str2.lower()

    freq_str1 = {}
    freq_str2 = {}


    for char in str1_lower:
        freq_str1[char] = freq_str1.get(char, 0) + 1

    for char in str2_lower:
        freq_str2[char] = freq_str2.get(char, 0) + 1


    common_characters = [char for char in freq_str1 if char in freq_str2 and freq_str1[char] == freq_str2[char]]

    common_characters.sort()

    return common_characters



str1 = "aabbcc"
str2 = "abbcc"
print(find_common_characters(str1, str2))

str1 = "Hello, World!"
str2 = "world: hello!"
print(find_common_characters(str1, str2))
