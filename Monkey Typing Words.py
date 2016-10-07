import random
y=0
while y<5:
        B=[]
        C=[6,15,15,4] 
        #'6,15,15,4'=food
        n=0
        while 1:
                x=random.randint(1,26)
                B.append(x)
                x=random.randint(1,26)
                B.append(x)
                x=random.randint(1,26)
                B.append(x)
                x=random.randint(1,26)
                B.append(x)
                n=n+1
                if B==C:
                        break
                else:
                        B=[]
        print(n)
        y=y+1
