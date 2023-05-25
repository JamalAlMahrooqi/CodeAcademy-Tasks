# # def fibonacci_numbers(nums):
# #     x,y=0,1
# #     for i in range(nums):
# #         x,y=y,x+y
# #         yield x
# #         
# # def square(nums):
# #     for num in nums:
# #         yield num**2
# # 
# # def cube(nums):
# #     for i in nums:
# #         yield i**3
# # print(sum(square(fibonacci_numbers(10))))     
# # print(sum(cube(square(fibonacci_numbers(10)))))
# 
# # def even_numbers(num):
# #     for i in num:
# #         if i%2==0:
# #             yield i
# # x=even_numbers([1,2,3,4,5,6,7,8,9,10])
# # for i in x:
# #     print(i,end=' ')
# #
# 
# # def func1(fun):
# #     def wrapper():
# #         print("Hello")
# #         fun()
# #         print("Welcome to pyhton")
# #     return wrapper
# # 
# # def func2():
# #     print("Code Academy")
# #     
# # f=func1(func2)
# # f()
# 
# import time
# import math
# 
# def calculate_time(func):
#     def wrapper(n):
#         begin=time.time()
#         func(n)
#         end=time.time()
#         print("Time taken in: ",
#               func.__name__,end-begin)
#     return wrapper
# 
# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))
# 
# factorial(10)
# 
#
