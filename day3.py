N = int(input())
    
if N >=1 and N <= 100 :
        if N % 2 == 0 :
            if N in range(2,5):
                print("Not Weird")
            elif N in range(6,21):
                print("Weird")
            if N > 20:
                print("Not Weird")
        else:
            print("Weird")
else:
    print(0)