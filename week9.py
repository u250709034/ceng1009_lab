#-----------EXERCİSE 1 -------------
# def is_odd(n):
#     return n % 2 == 1
#
# number = int(input("Enter a number: "))
# print(is_odd(number))


#-----------EXERCİSE 2 -------------

# def is_leapyear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
# year = int(input("Enter a year: "))
# print(is_leapyear(year))


#-----------EXERCİSE 3 -------------

# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#         print(i , total)
#
# sayi = int(input("Enter a number: "))
# print(print_triangular_numbers(sayi))

#-----------EXERCİSE 4 -------------

# def is_prime(n):
#     if n < 2:
#         return False
#     for  i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
#
# sayi = int(input("Enter a number: "))
# print(is_prime(sayi))


#-----------EXERCİSE 5 -------------

# def reverse(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result
#
# yazi = str(input("Print something : "))
# print(reverse(yazi))
#
# def reverse_slice(s):
#      s[::-1]
# print(reverse_slice("hello world"))


#-----------EXERCİSE 6 -------------

# def remove_all_occurences(sub,s):
#
#     return s.replace(sub,"")
#
# print(remove_all_occurences("l", "Hello world"))

#-----------EXERCİSE 7 -------------
#
# def substitute(message, key):
#     alphabet= "abcçdefgğhıijklmnoöprsştuvyz"
#     result= ""
#     for ch in message:
#         index= alphabet.find(ch.lower())
#         if index== -1:
#             result= result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key= "tgdjeopmnrstşüupzvyabğcfçlköhıi"
# print(substitute("hello, world!", key))
# ----------EXERCİSE 8 ----------------
# 
# def remove_dups(s):
#     result=""
#     for ch in s:
#         if ch.lower()  not in result.lower():
#             result= result + ch
#     return result
# 
# print(remove_dups("Hello World!"))
