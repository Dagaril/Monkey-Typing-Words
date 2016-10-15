import random
import math
wrd=list(input('Enter your word: '))
A=[];B=[];C=[]
y=0
atmpt=10
I=[0,0,0,0,0,0]
cntr=1
def rndmltr():
    x=random.randint(97,122)
    A.append(x)
    return A
for letter in wrd:
    num= ord(str.lower(letter))
    B.append(num)
#^Creates a list 'B' which consists of the numerical code for the entered letters
for y in range(atmpt):
    n=0
    while 1:
        for m in range(len(wrd)):
            rndmltr()
        #^Generates random integers as many times as there are letters in the entered word
        n+=1
        if A==B:
            if n<10000:
                I[0]+=1
            else:
                if n>50000:
                    I[5]+=1
                else:
                    for h in range(20000,60000,10000):
                        if n<=h:
                            I[cntr]+=1
                            cntr=1
                            break
                        cntr+=1
            A=[]
            break
        else:
            A=[]
    C.append(n)
    print(n)
print(I)
