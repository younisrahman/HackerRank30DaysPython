# T = int(input())

# for i in range(T):
#     N = int(input())
#     # prime number
#     if N == 1:
#         print('Not prime')
#     elif N == 2:
#         print('Prime')
#     else:
#         for i in range(3, int(N**(1/2))+1, 2):
#             # print(f" current number is ${ int(N**(1/2))+1 }")
#             if N % i == 0:
#                 print("Not prime")
#                 break
#         else:
#             print('Prime')


for _ in range(int(input())):
    num = int(input())
    if(num == 1):
        print("Not prime")
    else:
        if(num % 2 == 0 and num > 2):
            print("Not prime")
        else:
            for i in range(3, int(num**(1/2))+1, 2):
                if num % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")
