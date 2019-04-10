def twoparm(a='', *args):

    sum = 0
    leth = 0

    for i in args:
        sum += i
        leth += 1
    print(sum)
    print(leth)
    print(a)

    if a <= leth:
        print('False')
    elif a > leth:
        print('True')


#twoparm(8,5,6,8,7,9,4,5)


def add(a='', b=''):
    a += b
   #print(sum)


#add(7, 5)




def mull(c='', d=''):
    sum2 = 0
    for n in range(d):
        sum2 += c


    print(sum2)


mull(7, 8)
