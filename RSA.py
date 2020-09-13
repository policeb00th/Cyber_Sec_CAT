from sympy.ntheory.factor_ import totient
from Euclidean_GCD import Extended_Euclidean
from Euclidean_GCD import Extended_Euclidean_quiet


def Encrypt(e, P, n=0):
    Cript = (P**e) % n
    print(f"Criptext= P^e mod(n)={P}^{e} mod({n})={Cript}")
    return Cript


def Decrypt(d, C, n=0):
    Dcript = (C**d) % n
    print(f"Dcript= C^d mod(n)={C}^{d} mod({n})={Dcript}")
    return Dcript


def RSA():
    n = int(input("Enter n if provided, else enter 0: "))
    p = 0
    q = 0
    if n == 0:
        p = int(input("Enter p: "))
        q = int(input("Enter q: "))
        n = p*q
        print(f"n=p*q={p}*{q}={n}")
    phin = totient(n)
    print(f"phi({n})={phin}")
    e = int(input("enter e if provided, else enter 0: "))
    if(e == 0):
        d = int(input("enter d"))
        e = Extended_Euclidean_quiet(phin, d)
        print(f"e=d^-1 mod(phi(n))={d}^-1 mod({phin})={e}")
    else:
        d = Extended_Euclidean_quiet(phin, e)
        print(f"d= e^-1 mod(phi(n))= {e}^-1 mod({phin})= {d}")
    choice = int(input("Enter 0 to Encrypt, 1 to Decrypt, 2 to do both: "))
    if(choice == 0):
        P = int(input("Enter plaintext integer sequence to encrypt: "))
        Encrypt(e, P, n)
    elif(choice == 1):
        C = int(input("Enter ciphertext integer sequence to decrypt: "))
        Decrypt(d, C, n)
    elif(choice == 2):
        P = int(input("Enter plain text to first encrypt and then decrypt: "))
        C = Encrypt(e, P, n)
        Decrypt(d, C, n)
