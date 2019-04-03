def sumarry():

    array = [17, 1, 12, 54, 23, 9, 21]
    sumarray = []
    for i in array:
        if i >= 3 and i <= 20:
          sumarray.append(i)

    print(sum(sumarray))


sumarry()


def sumval():

    val1 = 0
    val2 = 0
    integ = []
    while True:
        num = int(input("Enter a Number: "))
        integ.append(num)

        if val1 <= 10:
            val1 += num
            val2 += num
        elif val2 <= 30:
            val2 += num
        else:
            break


    integ = sum(integ)
    print(val1, val2, integ)
    print(val1 + val2 + integ)


sumval()


def sumval2():

    nums = []

    while True:
        num1 = int(input("Enter a Number: "))
        nums.append(num1)

        if num1 > 10:
            break
        elif (sum(nums)) > 30:
            break


    print(sum(nums))


sumval2()




