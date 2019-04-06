
def numinp():

    num_arry = []
    num = 0

    while num <= 10:
        num = int(input('Enter a Number: '))
        num_arry.append(num)

    num_arry = list(set(num_arry))

    #for n in num_arry:
    #    print(n)
    #    num_arry.remove(n)
    while len(num_arry) > 0:
        print(num_arry.pop())




numinp()