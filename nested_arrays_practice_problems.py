#  1. Use a nested loop to convert an array of number pairs into a single flattened array.
#     For example, [[1, 3], [8, 9], [2, 16]] becomes [1, 3, 8, 9, 2, 16].

# list = [[1, 3], [8, 9], [2, 16]]
# new_list = []

# for group in list:
#     for n in group:
#         new_list.append(n)

# i = 0
# while i < len(list):
#     j = 0
#     while j < len(list[i]):
#         new_list.append(list[i][j])
#         j += 1
#     i += 1

# print(new_list)

#  2. Use a nested loop with two arrays of strings to create a new array of strings with each string combined.
#     For example, ["a", "b", "c"] and ["d", "e", "f", "g"] becomes ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"].

# l1 = ["a", "b", "c"]
# l2 = ["d", "e", "f", "g"]
# list = []

# for w1 in l1:
#     for w2 in l2:
#         list.append(w1 + w2)

# i = 0
# while i < len(l1):
#     j = 0
#     while j < len(l2):
#         list.append(l1[i] + l2[j])
#         j += 1
#     i += 1

# print(list)

#  3. Use a nested loop with one array of strings to create a new array that contains every combination of each string with every other string in the array.
#     For example, ["a", "b", "c", "d"] becomes ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"].

# list = ["a", "b", "c", "d"]
# new_list = []

# for l1 in list:
#     for l2 in list:
#         if l1 != l2:
#             new_list.append(l1 + l2)

# i = 0
# while i < len(list):
#     j = 0
#     while j < len(list):
#         if list[i] != list[j]:
#             new_list.append(list[i] + list[j])
#         j += 1
#     i += 1

# print(new_list)

#  4. Use a nested loop to find the largest product of any two different numbers within a given array.
#     For example, [5, -2, 1, -9, -7, 2, 6] becomes 63.

# list = [5, -2, 1, -9, -7, 2, 6]
# largest = list[0]

# for i in list:
#     for j in list:
#         if i != j:
#             if (i * j) > largest:
#                 largest = (i * j)

# i = 0
# while i < len(list):
#     j = 0
#     while j < len(list):
#         if i != j:
#             if (list[i] * list[j]) > largest:
#                 largest = list[i] * list[j]
#         j += 1
#     i += 1

# print(largest)

#  5. Use a nested loop to compute the sum of all the numbers in an array of number pairs.
#     For example, [[1, 3], [8, 9], [2, 16]] becomes 39.

# list = [[1, 3], [8, 9], [2, 16]]
# sum = 0

# for group in list:
#     for n in group:
#         sum += n

# i = 0
# while i < len(list):
#     j = 0
#     while j < len(list[i]):
#         sum += list[i][j]
#         j += 1
#     i += 1

# print(sum)

#  6. Use a nested loop with two arrays of numbers to create a new array of the sums of each combination of numbers.
#     For example, [1, 2] and [6, 7, 8] becomes [7, 8, 9, 8, 9, 10].

# l1 = [1, 2]
# l2 = [6, 7, 8]
# list = []

# for n1 in l1:
#     for n2 in l2:
#         list.append(n1 + n2)

# i = 0
# while i < len(l1):
#     j = 0
#     while j < len(l2):
#         list.append(l1[i] + l2[j])
#         j += 1
#     i += 1

# print(list)

#  7. Use a nested loop with an array of numbers to compute an array with every combination of products from each number.
#     For example, [2, 8, 3] becomes [4, 16, 6, 16, 64, 24, 6, 24, 9].

# list = [2, 8, 3]
# new_list = []

# for i in list:
#     for j in list:
#         new_list.append(i * j)

# i = 0
# while i < len(list):
#     j = 0
#     while j < len(list):
#         new_list.append(list[i] * list[j])
#         j += 1
#     i += 1

# print(new_list)

#  8. Use a nested loop to find the largest sum of any two different numbers within an array.
#     For example, [1, 8, 3, 10] becomes 18.

# list = [1, 8, 3, 10]
# largest = list[0]

# for i in list:
#     for j in list:
#         if i != j:
#             if (i + j) > largest:
#                 largest = i + j

# i = 0
# while i < len(list): # not complete
#     j = 0
#     while j < len(list):
#         if i != j:
#             if (i + j) > largest:
#                 largest = i + j
#         j += 1
#     i += 1

# print(largest)

#  9. Use nested loops with an array of numbers to compute a new array containing the first two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.
#     For example, [2, 5, 3, 1, 0, 7, 11] becomes [3, 7].

# 10. Use a nested loop to convert an array of string arrays into a single string.
#     For example, [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]] becomes "amanaplanacanalpanama".


# SOLUTIONS: https://gist.github.com/peterxjang/af8985dc4fb07ea14b4bd6ba41cb08f8
