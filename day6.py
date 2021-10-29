number = int(input())

for i in range(0,number):
    n = str(input())
    str1 =n[0]
    str2 =""
    for j in range(1,len(n)):
        if j % 2 == 0 :
            str1 = str1+n[j]
        else :
            str2 = str2+n[j]
    print(f"{str1} {str2}")