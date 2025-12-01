# s=input("enter name : ")
# # new_s=""
# # print(s[3])
# li=[]
# for i in range(0,len(s),2):
#     cap=s[i].upper()
# print(li.append(cap),end="")
# else: 




# # li=["s","r","i"]
# # for i in li:
# #     print(i,end="")

# s = "1 2 2 3 4 5 6"
# # s = "".join(s.split())
# s = s.split(" ")
# print(s)
# s = " ".join(s)
# # s = sum(int(i) for i in s if int(i)%2 != 0)
# # n = 0
# # for i in s:
# #     if int(i)%2 != 0:
# #         n += int(i)
# print(s)
# # i = 0
# # while i != len(s):
# #     if i % 2 == 0:
# #         print(s[i].upper(),end="")
# #     elif i% 2 == 1:
# #         print(s[i].lower(),end="")
# #     i +=1


# # s = input("enter the number")
# # for ind, i in enumerate(s):
# #     if ind%2 == 0:
# #         print(i.upper(),end="")
# #     else:
# #         print(i.lower(),end="")
         

# class You:
#     @staticmethod
#     def me(n):
#         print(f"function me : {n}")

# You.me(10)

# def me(fun):
#     def hi(n):
#         if n%2 == 0:
#             print("even")
#         else:
#             print("odd")
#         fun(n)

#     return hi


# @me
# def you(n):
#     print(n*n)


# you(6)

# class mat:
#     def adds(a,b):
#         return a+b
#     def muls(a,b):
#         return a*b



# s = input("enter name : ")

# li = []

# for i in range(0, len(s), 2):
#     li.append(s[i].upper())

# print("".join(li))



s=input("enter string: ")
# new_str=""
# for i in range(len(s)):
#     print(i)
#     if i%2==0:
#         new_str+=s[i].upper()
#     else:
#         new_str+=s[i].lower()
# print(new_str)

result=""
for i in range((len(s))):
    m=i%4
    if m<2 and s[i]!=" ":
        result+=s[i].upper()
    else:
        result+=s[i].lower()
print(result)