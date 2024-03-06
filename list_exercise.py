# Task
#
# Consider a list (list = [] ).You can perform the following commands:
# 1. insert i e: Insert integer e at position i .
# 2. pri nt : Print the list.
# 3. remove e : Delete the first occurrence of integer e.
# 4. append e : Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where
# each command will be of the 7 types listed above. Iterate through each command in
# order and perform the corresponding operation on your list.
# Example
# N = 4
# append 1
# append 2
# insert 3 1
# print
# • append 1: Append 1 to the list, arr = [l ].
# • append 2: Append 2 to the list, arr = [l , 2].
# • insert 3 1: lnsert 3 atindex l,arr = [1, 3,2].
# • print: Print the array.
# Output:
# [1, 3, 2 ]
#
# Input Format
# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.
# Constraints
# • The elements added to the list must be integers.
#
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input O
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
#
# Sample Output O
#
# [6, 5, 10)
# [1, 5, 9, 10)
# [9, 5, 1)

# solution

if __name__ == '__main__':
    N = int(input())
    nums = []
    for _ in range(N):
        commands = input().split()
        if commands[0] == 'append':
            eval(f'nums.append(int(commands[1]))')
        elif commands[0] == 'insert':
            eval(f'nums.insert(int(commands[1]), int(commands[2]))')
        elif commands[0] == 'remove':
            eval(f'nums.remove(int(commands[1]))')
        elif commands[0] == 'print':
            print(nums)
        else:
            eval(f'nums.{commands[0]}()')

