!#/usr/bin/env python3
def full_name():
    fname = input('First name: ')
    lname = input('Last name: ')
    print('Hello ' + fname + ' ' + lname)


full_name()


def calc():
    fnum = input('enter number: ')
    snum = input('second number: ')
    fnum = int(fnum)
    snum = int(snum)

    print(f'{fnum} + {snum} =', fnum + snum, '\n' f'{fnum} * {snum} =', fnum * snum, '\n'
          f'{fnum} / {snum} =', fnum / snum)
    if fnum == snum:
        print('the numbers are Equal')

    print(f'{fnum} + {snum} =', fnum + snum, '\n', f'{fnum} * {snum} =', fnum * snum, '\n',
          f'{fnum} / {snum} =', fnum / snum)
    if fnum == snum:
        print('Equal')

    elif fnum > snum:
        print(fnum)
    elif fnum < snum:
        print(snum)


calc()


def twoandone():
    str1 = input('enter a word: ')
    str2 = input('second word: ')
    num = input('enter number 1-3: ')
    num = int(num)
    str4 = (str1 + str2 + f'{num}')
    if str1 > str2:
        print(str1)
        str3 = (str1[0:num])
        fchar2 = (str2[0])
        print(str1.replace(fchar2, 'golan'))
    elif str1 == str2:
        print('Equal')
    else:
        print(str2)
        str3 = (str2[0:num])
        fchar1 = (str1[0])
        print(str2.replace(fchar1, 'golan'))

    print(str3)

    acount = 0

    for i in str4:
        if i == 'A':
            acount += 1

    print(acount)


twoandone()


def threarr():
    st1 = input('1st string: ')
    st2 = input('2nd string: ')
    st3 = input('3rd string: ')
    arr = [st1, st2, st3]



threarr()

    str4 = (str4.find('A'))
    print(len(f'str4'))




twoandone()

