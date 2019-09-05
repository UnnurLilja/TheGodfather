n=int(input("Enter the length of the sequence: "))
count_number=0
num1=1
num2=2
num3=3
while count_number<n:
    if count_number==0:
        summa=num1
        print(summa)
    elif count_number==1:
        summa=num1+1
        print(summa)
    elif count_number==2:
        summa=num1+num2
        print(summa)
    else:
        summa=num1+num2+num3
        num1=num2
        num2=num3
        num3=summa
        print(summa)
    count_number+=1