''' Данная программа сортирует 2 файла(по отдельности), а затем
    соединяет их в один тоже отсортированный файл.
'''    

def sortt(f):
    F = open('exe.txt')
    h = open('H.txt','w')
    h1 = open('H1.txt','w')
    while F.readline():
        F.seek(0)
        minf = int(F.readline())
        for line in F:
            if int(line)<minf:
                minf = int(line)
        F.close()        
        F = open(f)
        for line in F:
            if int(line)==minf:
                h.write(line)
            else:
                h1.write(line)
        h1.close()
        h1 = open('H1.txt')
        F.close()
        F = open(f,'w')
        for line in h1:
            F.write(line)
        F.close()
        h1.close()
        F = open(f)
        h1=open('H1.txt','w')
    F.close()
    h.close()
    h1.close()
    h = open('H.txt')
    F = open(f,'w')
    for line in h:
        F.write(line)
        print(line)
    F.close()
    h.close()
sortt('exe.txt')
##def printt(f):
##    F = open(f)
##    print(f,':')
##    for i in F:
##        print(i,end='')
##    F.close()    

##sortt('P1.txt')
##P = open('P.txt')
##kp = 0
##for i in P:
##    kp += 1
##P.close()
##P1 = open('P1.txt')
##kp1=0
##for i in P1:
##    kp1 += 1
##P1.close()
##
##
##P = open('P.txt')
##P1 = open('P1.txt')
##i = j = 0
##P2 = open('P2.txt','w')
##
##''' Процесс склеивания двух файлов в один'''
##a = P.readline()
##b = P1.readline()
##
##while i <=(kp-1) and j<=(kp1-1):
##    if a and b and int(a)<int(b) :
##        P2.write(a)
##        i+=1
##        if i==kp:
##            break
##        a = P.readline()
##    elif  a and b and int(a)==int(b):
##        P2.write(a)
##        P2.write(b)
##        i+=1
##        j+=1
##        if i==kp or j==kp1:
##            break
##        a = P.readline()
##        b = P1.readline()        
##    else:
##        P2.write(b)
##        j+=1
##        if j ==kp1:
##            break
##        b = P1.readline()
##while i<=(kp-1):
##    P2.write(a)
##    i+=1
##    a=P.readline()
##while j<=(kp1-1):
##    P2.write(b)
##    j+=1
##    b = P1.readline()
##P.close()
##P1.close()
##P2.close()
##
##P2 = open('P2.txt')
##h = open('H.txt','w')
##i = 0
##fib1= fib2 = povtch = 1
##while i<=(kp+kp1-1):
##    a = P2.readline()
##    while int(a)>fib1:
##        fib1,fib2 = fib1+fib2,fib1
##    if int(a)==fib1:
##        h.write(a)
##    i+=1
##P2.close()
##h.close()
##printt('H.txt')                
##printt('P.txt')
##printt('P1.txt')
##printt('P2.txt')
                                                                                                                                                                                                                                                                                                                                               '])
		f.close()
                        
        
    elif choice == '5':
        if filename == '':
            print('БД не создана')
        else:
           
            if number == 0:
                print('БД - пуста')
            else:
		f = open(filename,'rb')
                key1, value1 = input('Введите 1 поле и его значение: ').split()
                while key1 not in struct.keys():
                        print('Данного поля не существует')
                        key1 = input('Введите новое 1 поле: ')
                while value1 not in struct.values():
                        print('Данного значения поля не существует')
                        value1 = input('Введите новое значение 1 поля: ')

                key2, value2 = input('Введите 1 поле и его значение: ').split()
                while key2 not in struct.keys():
                        print('Данного поля не существует')
                        key2 = input('Введите новое 2 поле: ')
                while value2 not in struct.values():
                        print('Данного значения поля не существует')
                        value2 = input('Введите новое значение 2 поля: ')
		print('Найденные поля: ')
                for i in range(number):
                    struct = p.load(f)
                    if struct[key1] == value1 and struct[key2] == value2 :
                        print(struct['Книга'],struct['Автор'],\
                        struct['Наименование'], struct['Год издания'])
                f.close()        

    else:
        print('Введённого номера нет')
