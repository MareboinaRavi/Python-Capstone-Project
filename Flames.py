name1 = input("enter name1 :").lower().replace(" ","")
name2 = input("enter name2 :").lower().replace(" ","")

for i in name1:
    for j in name2:
        if(i==j):
            name1 =name1.replace(i,"",1)
            name2 =name2.replace(i,"",1)
            break
count = len(name1 + name2)
#print("count is ",count)
if count>0:
    listt = ["Friends" , "Lovers" ,"Affectionate", "Marriage","Enemies","Siblings"]
    while(len(listt) > 1):
        c =  count % len(listt) 
        s_index = c - 1
        if(s_index >= 0):
            left = listt[:s_index]
            right = listt[s_index +1 :]
            listt = left + right
        else:
            listt =listt[:len(listt)-1]
    print("your both are" , listt[0] ,"According to FLAMES")
else:
    print("They are One-close to other")
    
