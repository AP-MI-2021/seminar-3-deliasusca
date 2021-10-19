from math import sqrt

def read_list():
    n=int(input("Introduceti nr de elemente: "))
    lst=[]
    for i in range(n):
        x=int(input("a[{}]= ".format(i+1)))
        lst.append(x)
    return lst

def nr_div_proprii(n):
    nr_div_pr=0
    for i in range(2,n//2+1):
        if n%i==0:
            nr_div_pr+=1
    return nr_div_pr

def test_nr_div_proprii():
    assert nr_div_proprii(13)==0
    assert nr_div_proprii(18)==4
    assert nr_div_proprii(14)==2

test_nr_div_proprii

def adaug_div_prop(lst):
    rez=[]
    for x in lst:
        rez.append(x)
        rez.append(nr_div_proprii(x))
    return rez

def test_adaug_div_prop():
    assert nr_div_proprii([13, 9])==[13, 0, 9, 1]
    assert nr_div_proprii([1, 2, 18])==[1,0,2,0,18,4]

test_adaug_div_prop


def med_aritm(lst):
    suma=0
    for x in lst:
        suma=suma+x
    return round(suma/len(lst), 2)

def test_med_aritm():
    assert med_aritm([10, -3, 25, -1, 3, 10, 18]) == 8.86
    assert med_aritm([1,2,3]) == 2

test_med_aritm()

def list_med_aritm(lst, n):
    if med_aritm(lst)>float(n):
        return "DA"
    else:
        return "NU"

def test_list_med_aritm():
    assert list_med_aritm([10, -3, 25, -1, 3, 10, 18], 5) == "DA"
    assert list_med_aritm([1,2,3], 10) == "NU"

test_list_med_aritm()

def is_prime(n):
    if n<2:
        return False
    if n!=2 and n%2==0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def test_is_prime():
    assert is_prime(12)==False
    assert is_prime(2) == True
    assert is_prime(13) == True
    assert is_prime(1) == False
    assert is_prime(-65) == False
    assert is_prime(0) == False
    assert is_prime(9) == False

test_is_prime()

def list_elim_nr_prime(lst):
    i=0
    rez=[]
    while i<len(lst):
        if is_prime(lst[i])==False:
            rez.append(lst[i])
        i=i+1
    return rez

def test_list_elim_nr_prime():
    assert list_elim_nr_prime([4, 2, 5, 6, -7, 8]) == [4, 6, -7, 8]
    assert list_elim_nr_prime([0, -8, 5, 9]) == [0, -8, 9]
    assert list_elim_nr_prime([1, 13, 14, -4, 3, 6]) == [1, 14, -4, 6]

test_list_elim_nr_prime()

def show_menu():
    print("""
    1. Citire lista
    2. Afisarea listei dupa eliminarea numerelor prime
    3. Afisarea sumei primelor n numere pozitive
    4. Afisare "DA" daca toate numerele pozitive sunt in ordine crescatoare
    5. Numerele care apar o singura data sunt inlocuite cu numarul divizorilor proprii
    6. Afisare lista
    x. Iesire
    """)


def main():
    print(show_menu())
    lst=[]
    while True:
        cmd=input("Introduceti comanda: ")
        if cmd=='1':
            lst=read_list()
        elif cmd=='2':
            rez=list_elim_nr_prime(lst)
            print(rez)
        elif cmd=='3':
            n=int(input("Introduceti numarul: "))
            print(list_med_aritm(lst,n))
        elif cmd=='4':
            rez=adaug_div_prop(lst)
            print(rez)
        elif cmd=='5':
            pass
        elif cmd=='6':
            print(lst)
        elif cmd=='x':
            break
        else:
            print("Comanda invalida")

main()