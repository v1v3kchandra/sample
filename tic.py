from itertools import combinations 
import sys
print("==============Welcome to tictactoe ==================")
print(" ")
print(" ")
global tictac
tictac={11:11,12:12,13:13,21:21,22:22,23:23,31:31,32:32,33:33}
print("\t| ",tictac[11]," | ",tictac[12]," | ",tictac[13]," |")
print("\t|______|______|______|")
print("\t| ",tictac[21]," | ",tictac[22]," | ",tictac[23]," |")
print("\t|______|______|______|")
print("\t| ",tictac[31]," | ",tictac[32]," | ",tictac[33]," |")
print("\t|      |      |      |")
print(" ")
x=[{11,12,13},{11,21,31},{11,22,33},{12,22,32},{21,22,23},{31,32,33},{13,23,33},{13,22,31}]
x1=[]
o1=[]
x2=[]
o2=[]
count=0
choice=input("Enter your weapon (X or O)")
if choice=="X":
    choice2="O"
else:
    choice2="X"
for i in range(9):
  
    if i%2==1:
        place=int(input(choice2+" Enter your choice"))
        c=choice2
    else:
        place=int(input(choice+" Enter your choice"))
        c=choice
    for i in tictac:
        #print(i)
        if place==i:
            #print("Entering...")
            tictac[i]=c+" "           
            if c=="X":
                x1.append(place)#x1.add(place)
                print(x1)
            else:
                o1.append(place)#o1.add(place)
                print(o1)
    print("\t| ",tictac[11]," | ",tictac[12]," | ",tictac[13]," |")
    print("\t|______|______|______|")
    print("\t| ",tictac[21]," | ",tictac[22]," | ",tictac[23]," |")
    print("\t|______|______|______|")
    print("\t| ",tictac[31]," | ",tictac[32]," | ",tictac[33]," |")
    print("\t|      |      |      |")
    print(" ")
    count=count+1
    combx=combinations(x1,3)
    for i in combx:
        x2.append(list(i))
    combo=combinations(o1,3)
    for i in combo:
        o2.append(list(i))
    for i in x:
        #print("i value",i)    
        k=set(i)
        #print(k)
        for j in x2:
            k1=set(j)
            #print("from combx")
            #print(k1)
            #print(k)
            if k1==k:
                print(" X is Winner!! ")
                sys.exit()
                break
            
        #print("going back to loop")
    for i in x:
        #print("i value",i)    
        k=set(i)
        #print(k)
        for j in o2:
            k1=set(j)
            #print("from combx")
            #print(k1)
            #print(k)
            if k1==k:
                print(" O is Winner!! ")
                sys.exit()
                break
if count>8:
    print("DRAW!!!!!")
    
   


    

    
    
        
    
    



