# Task
# Given an integer, n, perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird
# Input Format
#
# A single line containing a positive integer, n.
#
# Constraints
#
# Output Format
#
# Print Weird if the number is weird. Otherwise, print Not Weird.
#
# Sample Input
#
# 3
# Sample Output
#
# Weird
# Explanation
#
#
#  is odd and odd numbers are weird, so print Weird.
#
# Sample Input 1
#
# 24
# Sample Output 1
#
# Not Weird
# Explanation 1
#
#
# is greater than 20 and  is even, so it is not weird.

# Solution

if __name__ == '__main__':
    n = int(input().strip())

if n % 2 == 1:
    print("Weird")

if n % 2 == 0:
    if 2 <= n <= 5:
        print("Not Weird")
    if 6 <= n <= 20:
        print("Weird")
    if n > 20:
        print("Not Weird")
