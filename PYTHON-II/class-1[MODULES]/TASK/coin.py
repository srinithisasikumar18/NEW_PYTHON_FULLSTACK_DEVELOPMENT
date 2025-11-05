import random
head_counter=0
coin=["head","tail"]
for i in range(100):
    result=random.choice(coin)
    if result=="head":
        head_counter+=1
print("no of heads from 100 flips is:",head_counter)
print("no of heads from 100 flips is:",100-head_counter)
    