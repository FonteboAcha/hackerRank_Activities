# Task
# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given n scores. Store them in a list
# and find the score of the runner-up.
#
# Input Format
#
# The first line contains n. The second line contains an array of
# integers each separated by a space.
#
# Constraints
# - 2 <= n <= 10
# - -100 <= A[i] <= 100
#
# Output Format
#
# Print the runner-up score.
#
# Sample Input
#
# 5
# 2 3 6 6 5
# Sample Output
#
# 5
# Explanation
#
# Given list is [2, 3, 6, 6, 5] . The maximum score is 6, second maximum is 5.
# Hence, we print 5 as the runner-up score.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

result = list(set(arr))
result.sort(reverse=True)

print(result[1])

# another way could be to remove the max element of the set
# and print the next max
