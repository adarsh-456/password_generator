import random
from pass_generator_word import lrts, num, sp_sym 


print("Welcome to my password generator!")
lr=input("How many letters you what in  your passwaord: ")
digit=input("How many digits you what in  your passwaord: ")
sym=input("How many symbols you what in  your passwaord: ")
password=[]
i=0
j=0
k=0
while (i<int(lr)):
    password.append(random.choice(lrts))
    i+=1
while (j<int(digit)):
    password.append(random.choice(num))
    j+=1
while (k<int(sym)):
    password.append(random.choice(sp_sym))
    k+=1
#easy password
pass1 = ""
for char in password:
    pass1+=char
print(f"your easy password is: {pass1}")
#hard password
random.shuffle(password)
pass2 = ""
for char in password:
    pass2+=char
print(f"your hard password is: {pass2}")

    




 