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
    while (val1 != 10 and val2 != 30):
        integ.append(int(input("Enter a Number: ")))
        val1 += 1
        val2 += 1

    integ = sum(integ)
    print(val1 + val2 + integ)


sumval()


def sumval2():
    num1 = 0
    nums = []

    while num1 < 10 or numssum < 30:
        num1 = int(input("Enter a Number: "))
        nums.append(num1)
        numssum = sum(nums)

    print(sum(nums))


#sumval2()




