

def decimal_to_binary(dec):
    '''
    Transforma un nr din zecimal in binar.
    :param dec: nr dat in baza 10
    :return: nr in baza 2
    '''
    decimal = int(dec)
    print(decimal, " in Binary : ", bin(decimal))

def print_menu():

    print('1. Transformare numar din baza 10 in baza 2.')
    print('x. Ieșire.')


def main():
    lst = []
    while True:
        print_menu()
        option = input('Alegeți opțiunea: ')
        if option == '1':
            dec = input()
            result = decimal_to_binary(dec)
        elif option == 'x':
            break
        else:
            print('Opțiune invalidă, reîncearcă!')

main()


def test_decimal_to_binary():
    assert decimal_to_binary(32)==0b100000
    assert decimal_to_binary(123)==0b1111011
test_decimal_to_binary()
