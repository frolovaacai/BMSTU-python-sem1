#Найти площадь полной поверхности
#и объём правильной четырехугольной усечённой пирамиды
#если известны высота,длина нижнего и вершнего ребра
#Фролова иу7-16б
high = float(input('Введите верхнее ребро:'))
if high <0: #проверка ввода
    high = float(input('Введите верхнее ребро >0:'))
bottom = float(input('Введите нижнее ребро:'))
if bottom <0: #проверка ввода
    bottom = float(input('Введите нижнее ребро >0')
h = float(input('Введите высоту:'))
if h <0: #проверка ввода
    h = float(input('Введите высоту >0'))
shigh = high*high #найдем площадь верхнего основания усеч.пирамиды
slow = bottom*bottom #найдем площадь нижнего основания усеч.пирамиды
V = 1/3*h*(shigh+slow+ (shigh*slow)**0.5) # найдем объём пирамиды 
hmin=(h**2+(bottom-high)**2)**0.5 #найдём высоту боковой грани пирамиды
S=shigh+slow+4*0.5*(high+bottom)*hmin # найдём площадь поверхности пирамиды
print('Объём усечённой пирамиды: {:.3f}'.format(V))
print('Площадь поверхности усечённой пирамиды: {:.3f}'.format(S))

