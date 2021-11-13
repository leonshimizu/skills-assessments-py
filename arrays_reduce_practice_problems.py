#  1. Start with an array of numbers and compute the sum of all the numbers.
#     For example, [5, 10, 8, 3] becomes 26.

# list = [5, 10, 8, 3]
# sum = 0

# for n in list:
#     sum += n

# print(sum)

#  2. Start with an array of strings and combine them all into a single string.
#     For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

# list = ["volleyball", "basketball", "badminton"]
# string = ""

# for w in list:
#     string += w

# print(string)

#  3. Start with an array of hashes and compute the sum of the prices (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.

# dictionary = [{"name": "chair", "price": 100}, {
#     "name": "pencil", "price": 1}, {"name": "book", "price": 4}]
# sum = 0

# for product in dictionary:
#     sum += product["price"]

# print(sum)

#  4. Start with an array of numbers and compute the the minumum number.
#     For example, [5, 10, 8, 3, 9] becomes 3.

# list = [5, 10, 8, 3, 9]
# min = list[0]

# for n in list:
#     if n < min:
#         min = n

# print(min)

#  5. Start with an array of strings and compute the total length of all the strings.
#     For example, ["volleyball", "basketball", "badminton"] becomes 29.

# list = ["volleyball", "basketball", "badminton"]
# sum = 0

# for s in list:
#     sum += len(s)

# print(sum)

#  6. Start with an array of hashes and find the hash with the lowest price (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.

# dictionary = [
#     {
#         "name": "chair",
#         "price": 100
#     },
#     {
#         "name": "pencil",
#         "price": 1
#     },
#     {
#         "name": "book",
#         "price": 4
#     }
# ]
# lowest = dictionary[0]

# for product in dictionary:
#     if product["price"] < lowest["price"]:
#         lowest = product

# print(lowest)

#  7. Start with an array of numbers and compute product of all the numbers.
#     For example, [5, 10, 8, 3] becomes 1200.

# list = [5, 10, 8, 3]
# product = 1

# for n in list:
#     product *= n

# print(product)

#  8. Start with an array of strings and combine them all into a single string, separated by dashes.
#     For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

# list = ["volleyball", "basketball", "badminton"]
# string = "-"

# for s in list:
#     string += s + "-"

# print(string)

#  9. Start with an array of hashes and find the hash with the shortest name (from the :name key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

# dictionary = [
#     {
#         "name": "chair",
#         "price": 100
#     },
#     {
#         "name": "pencil",
#         "price": 1
#     },
#     {
#         "name": "book",
#         "price": 4
#     }
# ]
# shortest = dictionary[0]

# for product in dictionary:
#     if len(product["name"]) < len(shortest["name"]):
#         shortest = product

# print(shortest)

# 10. Start with an array of numbers and compute the maximum number.
#     For example, [5, 10, 8, 3] becomes 10.

# list = [5, 10, 8, 3]
# max = list[0]

# for n in list:
#     if n > max:
#         max = n

# print(max)

# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/376c8931a48549889eb3c9bc091e9f43
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/379c9945774f51027750c59d6e4395df
# SOLUTIONS (using .reduce shortcut): https://gist.github.com/peterxjang/b69183e2d555964ce3936893f423ef35
