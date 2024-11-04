print("welcome to love calculate ")
name1=input("Enter the first person name.\n")
name2=input("Enter the second person name.\n")
name = (name1.lower()+name2.lower())
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
true=str(t+r+u+e)

l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
love=str(l+o+v+e)
score=int(true+love)

if (score<=0 and score<10) or (score >90 and score<=100):
    print("your score is " ,score, "you go together like coke annd  mentos.")
elif score>40 and score<=50:
    print("your score is ",score, "you are alright togrther")
else:
    print("your love score is " ,score)