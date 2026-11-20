# my_list = [76, 92.3, 'hello', True, 4, 76]
# my_list.append("apple")
# my_list.append(76)
# my_list.insert(3, "cat")
# my_list.insert(3,99)
# print(my_list.index("hello"))
# print(my_list.count(76))
# my_list.remove(76)
# my_list.pop(my_list.index(True))


# def sum_of_squares(number_list):
#     total = 0
#     for number in number_list:
#         total = total + number**2
#     return total
#
# my_list = [3, 4, 5]
# print(sum_of_squares(my_list))


# def sum_evens(number_list):
#     sum = 0
#     for number in number_list:
#         if number % 2 == 0:
#             sum+= number
#     return sum
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_evens(my_list))


# def count_five_letters(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
# my_list = ['apple', 'cat', 'lemon']
# print(count_five_letters(my_list))


# def sum_until_evens(number_list):
#     sum = 0
#     for number in number_list:
#         if number % 2 == 0:
#             break
#         sum += number
#     return sum
#
# my_list = [1, 3, 5, 7, 9, 10]
# print(sum_until_evens(my_list))


# def count_sam(words):
#     count = 0
#     for word in words:
#         count = count + 1
#         if word == 'sam':
#             break
#     return count
#
# my_list = ['ali', 'ayse', 'veli', 'mehmet', 'sam']
# print(count_sam(my_list))

# def replace(s, old, new):
#     pieces = s.split(old)
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual == expected:
#         if actual == expected:
#             print("Test passed")
#         else:
#             print("Test failed")
#
# test(replace('Mississippi', 'i', 'I' ),
#      'MIssIssIppI')

# def find_max_val_in_list(num_list):
#     max_val = num_list[0]
#     for num in num_list:
#         if num > max_val:
#             max_val = num
#     return max_val
#
# print(find_max_val_in_list([1,2,3,4,5,6,7,8,9,10]))
# print(find_max_val_in_list([-25, -96, 45, 0]))