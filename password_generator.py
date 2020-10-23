import random
lowercase = ['6','7','8','9', ',','&','*','!' ,'0','1','2','3','4','5','j','k','l','m','n','o','p','q', '1','2','3','4','5' ,'A','B','C','D','E','F','G','H','I','a','b','c','d','e','f','g','h','i','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
# uppercase = ['a','b','c','d','e','f','g','h','i','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# num = ['6','7','8','9','0','1','2','3','4','5']
#  special_chrs=[',','&','*','!',',','&','*','r','s','t','u','v','w','x','y','z']

n = int(input("enter the length of the password: "))
password = ''


while n != 0 :
    password = password + random.choice(lowercase)
    n = n - 1
# while n != 0 :
#     password = password + random.choice(random.choice(lowercase) + random.choice(uppercase) + random.choice(num) + random.choice(special_chrs))
#     n = n - 1

# password = random.choice(lowercase) + random.choice(uppercase) + random.choice(num) + random.choice(special_chrs)
# 
# password =  random.choice(num) + random.choice(special_chrs) + password + random.choice(lowercase)+ random.choice(uppercase) 

# print(random.choice(uppercase) + random.choice(num)  +password + random.choice(lowercase) + random.choice(special_chrs))

print(password)