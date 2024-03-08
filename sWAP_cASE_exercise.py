# Task
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#
# For Example:
#
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Function Description
#
# Complete the swap_case function in the editor below.
#
# swap_case has the following parameters:
#
# string s: the string to modify
# Returns
#
# string: the modified string
#
# Input Format
#
# A single line containing a string s.
#
# Sample Input 0
#
# HackerRank.com presents "Pythonist 2".
# Sample Output 0
#
# hACKERrANK.COM PRESENTS "pYTHONIST 2".

# solution

def swap_case(s):
    new = ''
    for n in s:
        if n.isupper():
            new += n.lower()
        else:
            new += n.upper()
    return new
# def swap_case(s):
#      return s.swapcase()
# does the same thing


if __name__ == '__main__':
    s = input()
    print(swap_case(s))
