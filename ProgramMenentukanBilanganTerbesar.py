print ('____________________________________')
print ('PROGRAM MENENTUKAN BILANGAN TERBESAR')
print ('____________________________________')
print ('')
print ('Masukkan 3 Bilangan yang diinginkan!')
a=int(input('Bilangan 1 = '))
b=int(input('Bilangan 2 = '))
c=int(input('Bilangan 3 = '))
if a>b and a>c:
    print('')
    print('=====================================')
    print (a, 'Adalah Bilangan terbesar')
elif b>a and b>c:
    print('')
    print('=====================================')
    print (b, 'Adalah Bilangan terbesar')
else:
    print('')
    print('=====================================')
    print(c, 'Adalah Bilangan terbesar')
    print('=====================================')
