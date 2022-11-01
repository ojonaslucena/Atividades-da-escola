a=input("Você telefonou para a vítima?\n")
b=input("Você esteve no local do crime?\n")
c=input("Você mora perto da vítima?\n")
d=input("Você devia para a vítima?\n")
e=input("Já trabalhou com a vítima?\n")
x=0
if a=="sim":
    x=x+1
if b=="sim":
    x=x+1    
if c=="sim":
    x=x+1
if d=="sim":
    x=x+1
if e=="sim":
    x=x+1
if x==2:
    print("Você é suspeito(a)!")
if x>2 and x<5:
    print("Você é cúmplice!")     
if x==5:
    print("Você é o(a) assassina!") 
if x==1:
    print("Você é inocente!")                     