f = open('mat_dv.txt')
krutoy={}
algebra={}
geoma={}
max1=0
max2-0
maxa=0
maxg=0

for line in f:
    s1=line.split()
    max2=int(s1[3])+int(s1[4])
    if max2>=max1:
        max1=max2
        krutoy[int(l[2])]=line+str(max1)
    if int(l[3])>=maxa:
        maxa=int(l[3])
        algebra[int(l[2])]=line+str(maxa)
    if int(l[4])>=maxg:
        maxg=int(l[4])
        geoma[int(l[2])]=line+str(maxg)


print('Pobeda po vsem 8',krutoy.get(8))
print('Pobeda po vsem 9',krutoy.get(9))
print('Pobeda po vsem 10',krutoy.get(10))
print('Pobeda po vsem 11',krutoy.get(11))
print('Pobeda po algebre 8',algebra.get(8))
print('Pobeda po algebre 9',algebra.get(9))
print('Pobeda po algebre 10',algebra.get(10))
print('Pobeda po algebre 11',algebra.get(11))
print('Pobeda po geometrii 8',geoma.get(8))
print('Pobeda po geometrii 9',geoma.get(9))
print('Pobeda po geometrii 10',geoma.get(10))
print('Pobeda po geometrii 11',geoma.get(11))
