import random
import math
wrd=list(input('Enter your word: '))
l=len(wrd)
A=[]
B=[]
C=[]
y=0
atmpt=100
def rndmltr():
    x=random.randint(97,122)
    A.append(x)
    return A
for letter in wrd:
    letter= str.lower(letter)
    num = ord(letter)
    B.append(num)
#^Creates a list 'B' which consists of the numerical code for the entered letters
while y<atmpt:
    n=0
    while 1:
        for m in range(l):
            rndmltr()
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
