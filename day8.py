n = int(input())

nameNumber = [input().split() for i in range(n)]
phoneBook = {k:v for k,v in nameNumber}
while True:
    try:
        name = input()
        if name in phoneBook:
            print('%s=%s' % (name, phoneBook[name]))
        else:
            print('Not found')
    except:
        break