def is_palindrome(nr):
    '''
    Determină dacă un număr dat este palindrom.

    :param nr: int, numarul dat
    :return: True daca este palindrom, False altfel
    '''
    inv= 0 #invers
    temp=nr
    while (nr!=0):
        inv=inv*10+nr%10
        nr//=10
    if (temp==inv):
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(132)==False
    assert is_palindrome(5669)==False
    assert is_palindrome(1221)==True
    assert is_palindrome(26)==False
    assert is_palindrome(15)==False
test_is_palindrome()

def is_prime(n):
    '''
    Programul determina daca un numar n este prim sau nu.
    -un numar intreg introdus de utilizator
    Output:
    -True daca numarul este prim sau False in caz contrar
    '''
    if(n < 2): return False
    if(n == 2): return True
    if(n % 2 == 0): return False
    i = 3
    while (i * i <= n):
        if n % i == 0:
          return False
        i = i + 2
    return True

def get_largest_prime_below(n):
    '''
    Subprogramul returneaza cel mai mic numar prim mai mic sau egal cu n
    Input:
    -un numar natural introdus de utilizator
    Output:
    -cel mai mic numar prim mai mic sau egal cu el
    -Daca nu exista, se va afisa mesajul "Nu exista"
    '''
    if n < 2: return "Nu exista"
    rez = n
    while rez >= 0:
        if is_prime(rez) == True:
            return rez
        rez = rez - 1

def test_get_largest_prime_below():
    '''
    Functia ce testeaza diferite exemple pentru get_largest_prime_below(ca la seminar)
    '''
    assert get_largest_prime_below(4) == 3
    assert get_largest_prime_below(7) == 7
    assert get_largest_prime_below(10) == 7
test_get_largest_prime_below()

def get_base_2(dec):
    '''
    Transforma un nr din zecimal in binar.
    :param dec: nr dat in baza 10
    :return: nr in baza 2
    '''
    decimal = int(dec)
    print(decimal, " in Binary : ", bin(decimal))

'''
def test_get_base_2():
    assert get_base_2(32)==32  in Binary :  0b100000
    assert get_base_2(123)==123  in Binary :  0b100000
test_get_base_2()'''


option = '''
Daca doriti sa aflati daca un numar este palindrom scrie 1.
Daca doriti sa aflati cel mai mic numar prim mai mic sau egal cu n scrie 2.
Daca doriti sa aflati valoare in baza 2 a numarului scrie 3.
Daca doriti sa opriti programul scrie 4.
'''

def main():
    while True:
        optiune = input(option)
        if optiune == '1':
            numar = int(input("Scrieti valoarea:"))
            if is_palindrome(numar):
                print("Este palindrom")
            else:
                print("Nu este palindrom")
        elif optiune == '2':
            numar = int(input("Scrieti valoarea:"))
            result = get_largest_prime_below(numar)
            print(result)
        elif optiune == '3':
            numar = int(input("Scrieti numarul: "))
            result = get_base_2(numar)
            return result
        elif optiune == '4':
            print("programul s-a oprit!")
            break
        else:
            print("Nu exista comanda!")

if __name__ == '__main__':
    main()



