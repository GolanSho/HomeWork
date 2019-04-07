
def numinp():

    num_arry = []
    num = 0

    while num <= 10:
        num = int(input('Enter a Number: '))
        num_arry.append(num)

    num_arry = list(set(num_arry))

    #for n in num_arry:
    #   print(num_arry.pop(0))

    while len(num_arry) > 0:
        print(num_arry.pop(0))


#numinp()


def studict():

    students = {1001: [10, 20, 30], 1002: [40, 60, 50], 1003: [90, 80, 70]}
    max = 0

    id = int(input('Enter an ID: '))
    if id in students:
        for i in students[id]:
            if i > max:
                max = i
    else:
        print('ID not exist')

    print(max)


#studict()


def suminarry():
    array = [2, 'Hello', ['Bye', [6, 3, 1, {'nums': [10, 20, 30]}]]]
    sum = 0
    while len(array[2][1][3]['nums']) > 0:
        num = array[2][1][3]['nums'].pop()
        num += sum
    print(sum)
    newarray = array[2][1][3]['nums'].insert(0, sum)

    print(newarray)

suminarry()