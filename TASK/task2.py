# s_marks=[50,45,60,75,75,80,100,74,99,1000,999]

# for mark in s_marks:
#     if mark<50:
#         print("fail")
#     elif mark>=50 and mark<75:
#         print("Pass")
#     elif mark>=75 and mark<=99:
#         print("good")
#     elif mark==100:
#         print("full")
#     else:
#         print("not valid")

s_marks=[50,45,60,75,75,80,100,74,99,1000,999]
result=[]
for mark in s_marks:
    if mark<50:
        # grade="fail"
        result.append("fail")
    elif mark>=50 and mark<75:
        result.append("pass")
    elif mark>=75 and mark<=99:
        result.append("good")
    elif mark==100:
        result.append("full")
    else:
        result.append("Not valid")
print(result)

# from one import mat as m

# print(m.adds(10,20))