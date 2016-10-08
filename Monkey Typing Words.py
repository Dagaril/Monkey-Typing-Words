import random
A=list(input('Enter your word: '))
l=len(A)
B=[]
y=0
for letter in A:
    num = ord(letter)
    if num<97:
            num=num+32
    B.append(num)
    print(B)
#^Creates a list 'B' which consists of the numerical code for the entered letters
while y<5:
        n=0
        while 1:
                for m in range(l):
                        x=random.randint(97,122)
                        A.append(x)
                #^Generates random integers as many times as there are letters in the entered word
                n+=1
                if A==B:
                        A=[]
                        break
                else:
                        A=[]
        print(n)
        y+=1
