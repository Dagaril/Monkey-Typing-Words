import random
import math
A=list(input('Enter your word: '))
l=len(A)
print (l)
B=[]
C=[]
y=0
atmpt=5
for letter in A:
    num = ord(letter)
    if num<97:
            num=num+32
    B.append(num)
    print(B)
A=[]
#^Creates a list 'B' which consists of the numerical code for the entered letters
while y<atmpt:
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
        C.append(n)
        y+=1
#Begin Confidence interval calculations
#mn=mean ; sd=standard deviation ; cl=confidence level ; cc=confidence coefficient ; me=margin of error ; ci=confidence interval
cl=.95
cc=1.96
mn=sum(C)/atmpt
print(mn)
sm=[]
for m in range(len(C)):
    sm.append((C[m]-mn)**2)
sd=math.sqrt((sum(sm)/atmpt))
me=cc*(sd/(math.sqrt(atmpt)))
ci1=mn-me
ci2=mn+me
print('95% of the attempts are between', ci1, 'and', ci2)
