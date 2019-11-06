PROGRAM MENENTUKAN BILANGAN TERBESAR

Pertama kita harus menginput bilangan pertama sampai bilangan ketiga. Codingnya :

a=int(input(‘Bilangan 1 = ‘))
b=int(input(‘Bilangan 2 = ‘))
c=int(input(‘Bilangan 3 = ‘))

Selanjutnya kita menggunakan logika if dan Logika AND. Codingnya :

if a>b and a>c:
print (a, ‘Adalah Bilangan terbesar’)
elif b>a and b>c:
print (b, ‘Adalah Bilangan terbesar’)
else:
print (c, ‘Adalah Bilangan terbesar’)
Penjelasannya : Jika a lebih dari b dan a lebih dari c, maka output bilangan a, kalau bilangan a bukan bilangan terbesar maka lanjut ke bilangan b, jika b lebih dari a dan b lebih dari c maka bilangan b Adalah Bilangan terbesar, kalau a dan b bukan bilangan terbesar maka bilangan c Adalah bilangan yang terbesar.

![2019-11-06 (1)](https://user-images.githubusercontent.com/57079848/68268481-f1c51a00-0088-11ea-9158-db6e1e004b8c.png)
