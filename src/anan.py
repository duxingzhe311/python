# #encoding: utf-8
# import math
# 
# def is_sushu(a):
#     if a < 2:
#         return False
#     for i in range(2,int(math.sqrt(a)) + 1):
#         if 0 == a % i:
#             return False
#     return True
# 
# print is_sushu(8)
# 
# a = list(filter(is_sushu, range(1,100)))
# 
# # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
# # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
# 
# print a
























# def isprime(m): 
#     for i in range(2, m/2+1): 
#         if m % i == 0: 
#             return False 
#     return True 
#  
# print filter(isprime, range(2,101)) 








def daYu5Ma(a):
    return a > 5
print daYu5Ma(7)






















