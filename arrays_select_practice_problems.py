#  1. Start with an array of numbers and create a new array with only the numbers less than 20.
#     For example, [2, 32, 80, 18, 12, 3] becomes [2, 18, 12, 3].

# list = [2, 32, 80, 18, 12, 3]
# new_list = []

# for n in list:
#     if n < 20:
#         new_list.append(n)

# print(new_list)

#  2. Start with an array of strings and create a new array with only the strings that start with the letter "w".
#     For example, ["winner", "winner", "chicken", "dinner"] becomes ["winner", "winner"].

# list = ["winner", "winner", "chicken", "dinner"]
# new_list = []

# for w in list:
#     if w[0].lower() == "w":
#         new_list.append(w)

# print(new_list)

#  3. Start with an array of hashes and create a new array with only the hashes with prices greater than 5 (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}].

# dictionary = [{"name": "chair", "price": 100}, {
#     "name": "pencil", "price": 1}, {"name": "book", "price": 4}]
# new_list = []

# for product in dictionary:
#     if product["price"] > 5:
#         new_list.append(product)

# print(new_list)

#  4. Start with an array of numbers and create a new array with only the even numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [2, 4, 8].

# list = [2, 4, 5, 1, 8, 9, 7]
# new_list = []

# for n in list:
#     if n % 2 == 0:
#         new_list.append(n)

# print(new_list)

#  5. Start with an array of strings and create a new array with only the strings shorter than 4 letters.
#     For example, ["a", "man", "a", "plan", "a", "canal", "panama"] becomes ["a", "man", "a", "a"].

# list = ["a", "man", "a", "plan", "a", "canal", "panama"]
# new_list = []

# for w in list:
#     if len(w) < 4:
#         new_list.append(w)

# print(new_list)

#  6. Start with an array of hashes and create a new array with only the hashes with names shorter than 6 letters (from the :name key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}, {name: "book", price: 4}].

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
# new_list = []

# for product in dictionary:
#     if len(product["name"]) < 6:
#         new_list.append(product)

# print(new_list)

#  7. Start with an array of numbers and create a new array with only the numbers less than 10.
#     For example, [8, 23, 0, 44, 1980, 3] becomes [8, 0, 3].

# list = [8, 23, 0, 44, 1980, 3]
# new_list = []

# for n in list:
#     if n < 10:
#         new_list.append(n)

# print(new_list)

#  8. Start with an array of strings and create a new array with only the strings that don't start with the letter "b".
#     For example, ["big", "little", "good", "bad"] becomes ["little", "good"].

# list = ["big", "little", "good", "bad"]
# new_list = []

# for w in list:
#     if w[0] != "b":
#         new_list.append(w)

# print(new_list)

#  9. Start with an array of hashes and create a new array with only the hashes with prices less than 10 (from the :price key).
#     For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "pencil", price: 1}, {name: "book", price: 4}].

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
# new_list = []

# for product in dictionary:
#     if product["price"] < 10:
#         new_list.append(product)

# print(new_list)

# 10. Start with an array of numbers and create a new array with only the odd numbers.
#     For example, [2, 4, 5, 1, 8, 9, 7] becomes [5, 1, 9, 7].

# list = [2, 4, 5, 1, 8, 9, 7]
# new_list = []

# for n in list:
#     if n % 2 == 1:
#         new_list.append(n)

# print(new_list)

# SOLUTIONS (using while loop): https://gist.github.com/peterxjang/7de16ed43ea506e98df3fa15074b84f8
# SOLUTIONS (using .each shortcut): https://gist.github.com/peterxjang/a702894841c7018ed8c127b647ae21f8
# SOLUTIONS (using .select shortcut): https://gist.github.com/peterxjang/b8c8fb8b77b2cae7bb9cc62a3a434761
