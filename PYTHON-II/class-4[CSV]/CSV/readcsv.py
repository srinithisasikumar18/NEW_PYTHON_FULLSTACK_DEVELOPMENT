# write a python script and read user.csv file
# and print all user names
import csv
with open('user.csv','r') as fp:
    csv_reader=csv.reader(fp)
    users=list(csv_reader)
    # print(csv_reader)
    # print(type(csv_reader))

    for user in users[1:]:
        print(type(user))
        print(user[1])


# import csv
# with open('user.csv','r') as fp:
#     csv_reader=csv.reader(fp)
#     users=list(csv_reader)
#     """ print(csv_reader)
#     print(type(csv_reader)) """

#     for user in users[1:]:
#         #print(type(user))
#         print(user[1])