def fine(returned, due):
    if returned[2] > due[2]:
        return 10000
    elif returned[2] < due[2]:
        return 0
    elif returned[1] > due[1]:
        return (returned[1] - due[1]) * 500
    elif returned[0] > due[0]:
        return (returned[0] - due[0]) * 15
    else:
        return 0


returned = list(map(int, input().rstrip().split()))
due = list(map(int, input().rstrip().split()))

print(fine(returned, due))
