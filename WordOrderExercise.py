# You are given  words. Some words may repeat. For each word,
# output its number of occurrences. The output order should correspond with
# the input order of appearance of the word.
# See the sample input/output for clarification.
#
# Note: Each input line ends with a "\n" character.
#
# Constraints:
#
# The sum of the lengths of all the words do not exceed
# All the words are composed of lowercase English letters only.
#
# Input Format
#
# The first line contains the integer, n.
# The next n lines each contain a word.
#
# Output Format
#
# Output  lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for
# each distinct word according to their appearance in the input.
#
# Sample Input
#
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Sample Output
#
# 3
# 2 1 1
# Explanation
#
# There are  distinct words. Here, "bcdef" appears twice in the
# input at the first and last positions.
# The other words appear once each.
# The order of the first appearances are "bcdef", "abcdefg" and "bcde"
# which corresponds to the output.

# Solution

num_of_words = int(input())

words = {}

for n in range(num_of_words):
    word = input()
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

print(len(set(words)))
print(" ".join(str(words[word]) for word in words))