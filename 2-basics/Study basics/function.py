# # # class emp:
# # #     """
# # #     this is a description for import a file form last directory
# # #     """
# # #     empcount=0
# # #     name="Elsayed"
# # #
# # #     def __init__(self,name,age,salary):
# # #         self.name=name
# # #         self.age=age
# # #         self.salary=salary
# # #         emp.empcount+=1
# # #
# # #     def Salary(self):
# # #         return self.salary
# # #
# # # emp1=emp("Ayman",20,500)
# # # emp2=emp("sara",18,1200)
# # # # print(emp2.Salary())
# # # # # emp1.pr=6
# # # # # del emp1.pr
# # # # # print(setattr(emp1,"age",50))
# # # # # print(emp1.age)
# # # # # delattr(emp1,"age")
# # # # # emp1.age=5
# # # # print(emp1.__dict__)
# #
# # class parent:
# #     def __init__(self):
# #         print("this is parent constructor")
# #
# #     def parentmethod(self):
# #         print("this is parent method")
# #
# # class child(parent):
# #     def __init__(self):
# #         print("this is child constructor")
# #
# #     def childmethod(self):
# #         print("this is child method")
# #     def __add__(self, other):
# #
# #
# #
# # ch=child()
# # ch.childmethod()
# # ch.parentmethod()
# # if issubclass(child,parent) and isinstance(ch,child):
# #     print("true")
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# class vector:
#     __s=5
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def __add__(self, other):
#         return vector(self.a+other.a,self.b+other.b)
#     def prs(self):
#         print(self.__s)
#
# v1=vector(2,10)
# v2=vector(3,5)
# v1.prs()
# # print(getattr(v1,"__s"))
a={5,6}
b={9,5}
print(a.isdisjoint(b))






