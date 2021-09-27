forleon = [1, 1]

def isInt(num):
    return int(num) == float(num)

def leon(num):
    global forleon

    if (num == 1):
        return True
    
    for i in range(num): 
        next = forleon[0] + forleon[1] + 1
        forleon[i % 2] = forleon[0] + forleon[1] + 1 
        if (next == num): 
            forleon = [1, 1] 
            return True 
    forleon = [1, 1] 
    return False 
    
def tau(num):
    amount = 0
    for i in range(num, 0, -1):
        if isInt(num / i):
            amount += 1
    return isInt(num / amount) if amount != 0 else False

def main(): 
    n = int(input('Введите размер массива: ')) 
    array = [None]*n 

    for i in range(n): 
        array[i] = int(input('Значение элемента‚ [' + str(i) + ']:'))

    for i in range(1, n):
        if (leon(array[i - 1]) and tau(array[i])) or (leon(array[i]) and tau(array[i - 1])):
            i += 1
            if (i >= n):
                break
            
            temp = array[i - 1]
            array[i - 1] = array[i]
            array[i] = temp
    
    print(array)




if (__name__ == '__main__'): 
    main()
