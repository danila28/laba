def Add(NValue):
    gall=InGallon(NValue)
    chel=288
    if gall>chel:
        chelder=gall//chel
        rem=gall%chel
        g=InBritain(rem)
        print('значение превышает 1 челдер- кол-во челдеров:',chelder,',квартеров:',g[0],',страйков:',g[1],',галлонов:',g[2])
    elif gall==chel:
        print('Значение равно 1-му челдеру')
    else:
        gall<chel
        rem=chel-gall
        g=InBritain(rem)
        print('До 1-го челдера нужно дополнить- квартеров:',g[0],',страйков:',g[1],',галлонов:',g[2])
        

def InGallon(NValue):
    gallon=NValue[2]
    strike=NValue[1]
    quarter=NValue[0]
    StrInGal=16
    QuarInGal=64
    return quarter*QuarInGal+strike*StrInGal+gallon

def InBritain(InGal):
    StrInGal=16
    QuarInGal=64
    quarter=InGal//QuarInGal
    remains=InGal%QuarInGal
    strike=remains//StrInGal
    gallon=remains%StrInGal
    Britain=[quarter, strike, gallon]
    return Britain


def Litr(NValue):
    galloninL=4.546    
    return InGallon(NValue)*galloninL


def Bushel(NValue):
    BushInL=36.36872
    return Litr(NValue)/BushInL


def Summ(NValue1, NValue2):
    SummGal=InGallon(NValue1)+InGallon(NValue2)
    g=InBritain(SummGal)
    print(g[0],'квартеров',g[1],'страйков',g[2],'галлонов')


def Difference(NValue1,NValue2):
    DiffGal=InGallon(NValue1)-InGallon(NValue2)
    g=InBritain(DiffGal)
    print(g[0],'квартеров',g[1],'страйков',g[2],'галлонов')


def Comparison(NValue1,NValue2):
    if InGallon(NValue1) > InGallon(NValue2):
        print('1 значение > 2 значения')
    elif InGallon(NValue1) < InGallon(NValue2):
        print('1 значение < 2 значения')
    else:
        print('1 значение = 2 значения')

def Num():
    while True:
        num=input("Введитете количество галлонов=>")
        try:
            num=int(num)
            if num >= 0 and num < 16:
                break
            else:
                print('Значение выходит за границы диапазона')
        except:
            if not num.isdigit():
                print('Введите числовое значение')
    return num


def Product(NValue, Num):
    ProdGal=InGallon(NValue)*Num
    g=InBritain(ProdGal)
    print(g[0],'квартеров',g[1],'страйков',g[2],'галлонов')

def Division(NValue, Num):
    DivGal=InGallon(NValue)/Num
    g=InBritain(DivGal)
    print(g[0],'квартеров',g[1],'страйков',g[2],'галлонов')


def Value():
    NValue=[]


    while True:
        quarter=input("Введитете количество квартеров=>")
        try:
            quarter=int(quarter)
            if quarter >=0 and quarter<=90:
                break
            else:
                print('Значение выходит за границы диапазона:')
        except:
            if not quarter.isdigit():
                print('Введите числовое значение:')


    while True:
        strike=input("Введитете количество страйков=>")
        try:
            strike=int(strike)
            if strike >= 0 and strike < 4:
                break
            else:
                print('Значение выходит за границы диапазона:')
        except:
            if not strike.isdigit():
                print('Введите числовое значение:')


    while True:
        gallon=input("Введитете количество галлонов=>")
        try:
            gallon=int(gallon)
            if gallon >= 0 and gallon < 16:
                break
            else:
                print('Значение выходит за границы диапазона:')
        except:
            if not gallon.isdigit():
                print('Введите числовое значение:')


    NValue=[quarter, strike, gallon]
    print('квартеров:',NValue[0],'страйков:',NValue[1],'галлонов:',NValue[2])
    return NValue
  



def main():
    print("программа над значениями объёма сыпучих материалов в британской системе мер:")
    punkt = '0'
    NuValue1=[0,0,0]
    NuValue2=[0,0,0]
    while(punkt != 'Q' and punkt != 'q'):
        if punkt == '0':
                print("\n0. Главное меню:",
"\nV1. Первое значение",
"\nV2. Второе значение",
"\nL1. Преобразование в литры первого значения",
"\nL2. Преобразование в литры второго значения",
"\nB1. Преобразование в бушели первого значения",
"\nB2. Преобразование в бушели второго значения",
"\nA1. Дополнение до максимального значения-челдера первого значения"
"\nA2. Дополнение до максимального значения-челдера второго значения"
"\nS.  Сумма первого и второго значения",
"\nD1. Разность первого и второго значения",
"\nD2. Разность второго и первого значения",
"\nC.  Сравнение",
"\nN.  Ввести число для операций деления и умножения",
"\nP1. Умножение на число первого значения",
"\nP2. Умножение на число второго значения",
"\nM1. Деление на число первого значения",
"\nM2. Деление на число второго значения",
"\nQ.  Выход")
        elif punkt == 'V1' or punkt == 'v1': NuValue1=Value()
        elif punkt == 'V2' or punkt == 'v2': NuValue2=Value()
        elif punkt == 'L1' or punkt == 'l1': print(Litr(NuValue1),'литров')
        elif punkt == 'L2' or punkt == 'l2': print(Litr(NuValue2),'литров')
        elif punkt == 'B1' or punkt == 'b1': print(Bushel(NuValue1),'бушелей')
        elif punkt == 'B2' or punkt == 'b2': print(Bushel(NuValue2),'бушелей')
        elif punkt == 'A1' or punkt == 'a1': Add(NuValue1)
        elif punkt == 'A2' or punkt == 'a2': Add(NuValue2)
        elif punkt == 'S' or punkt == 's': Summ(NuValue1, NuValue2)
        elif punkt == 'D1' or punkt == 'd1': Difference(NuValue1, NuValue2)
        elif punkt == 'D2' or punkt == 'd2': Difference(NuValue2, NuValue1)
        elif punkt == 'C' or punkt == 'c': Comparison(NuValue1, NuValue2)
        elif punkt == 'N' or punkt == 'n': num=Num()
        elif punkt == 'P1' or punkt == 'p1': Product(NuValue1, num)
        elif punkt == 'P2' or punkt == 'p2': Product(NuValue2, num)
        elif punkt == 'M1' or punkt == 'm1': Division(NuValue1, num)
        elif punkt == 'M2' or punkt == 'm2': Division(NuValue2, num)
        else:
            print("Такой команды нет")


        punkt = (input("Введите команду:>"))
        


if __name__ == '__main__':
    main()
