# # # a = 'ssafy'
# # # b = 'ssafy'
# # # c = 'ssafr'
# # #
# # # print(id(a))
# # # print(id(b))
# # # print(id(c))
# # #
# # # print(a is b)
# # # print(a == b)
# # #
# # # a= a.upper()
# # #
# # # print(id(a))
# # # print(id(b))
# #
# # # print('bbccaabca'.index('d'))
# # # print('dasdasdㅇ123'.isalpha())
# #
# # # '-30'isnumeric()
# # a = 'strabccc'
# # c = 'strab'
# # z = 'qwe'
# # # print(a.replace('c',z,0 ))
# #
# # # list = ['a', 'b','a', 'c', '123','a', [12345, 23]]
# # #
# # # print(list.pop(-2))
# # # print(list)
# #
# # # tuple1 = ('a', 'b', 'c')
# # # print(tuple1)
# # # print(id(tuple1))
# # # tuple1 += 1,2,3
# # # print(tuple1)
# # # print(id(tuple1))
# #
# # # def song():
# # #   print('song')
# # # print(song())
# # #
# # # def kim(a):
# # #     if a == "b":
# # #         print('kim')
# # #         print('sungjung')
# # #     print('able')
# # #
# # # kim('b')
# # # kim('a')
# #
# # # s = {'a', 'b', 'c', 'd'}
# # # t = 'abcdefg'
# # # # print(s.discard('a'))
# # # s.update(t)
# # # # print(s.issuperset(t))
# # #
# # # a = {range(2): 3,
# # #      (1,2): 4,
# # #      True: 7}
# # # # key는 immutable만 가능! set은 안된다!
# # # print(a)
# # #
# # # print(a.get(range(3), (1,2)))
# # #
# # # dicta = {'a':1, 'b':2, 'c':3, 'd':4}
# # # dicta.update(a=123)
# # # print(dicta)
# # # dicta.update(e=123123)
# # # print(dicta)
# #
# # # original = [1,2,3]
# # # copy = original
# # # print(original, copy)
# # #
# # # copy[0] = 'hello'
# # # print(original, copy)
# # #
# # # try:
# # #     print(t)
# # # except Error as err:
# # #
# # # finally:
# # #     print('abc is done')
# #
# # # raise EOFError
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def cover(self):
# #         return self.age
# #
# #
# # class Student(Person):
# #     def __init__(self, name, nle, age):
# #         super().__init__(name,age)
# #         self.nle = nle
# #         self.name = name
# #         self.age = age
# #
# # rony = Student('rony','nl',29)
# #
# # print(rony.cover())
# #
# #
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def cover(self):
# #         return(self.age)
# #
# #
# # class Student(Person):
# #     def __init__(self, name, nle, age):
# #         super().__init__(name,age)
# #         self.nle = nle
# #         self.name = name
# #         self.age = age
# #
# # rony = Student('rony','nl',29)
# #
# # print(rony.cover())
# a, b = 1,2
# def func1():
#     a, b = 3, 4
#     print(a, end=' ')
#     func2()
#
# def func2():
#     print(b, end=' ')
#
# func1()
# print(a)

# result = True + False
# print(result)