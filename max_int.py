# git init: tool sem við notum til að halda utan um breytingar, geymir allar breyringar
#sem gerðar voru við gerð kóðans
#git init: repository: staður þar sem git heldu rutan um breytingar á skölum
#forritun/class ls
#forritun/class git
# git commit    vista þessa breytingu
#git status: lýsa breytingunum sem áttu sér stað
number=int(input("Input a number: "))
max_number=0
while number>=0:
    print(number)
    
    number=int(input("Input a number: "))
    if number>max_number:
        max_number=number
    elif number<0:
        break
print("The maximum is: "+str(max_number))
