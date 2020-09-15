from ECC import mod
from Euclidean_GCD import Extended_Euclidean_quiet
def public_key_calculation(X,q,a):
    return mod(a**X,q)

def ElGamalEncrypt(Y,q,a,M,k):
    K=mod(Y**k,q)
    print(f"K=Y^k mod (q) = {K}")
    print(f"C1=a^K mod (q)")
    C1=mod(a**k,q)
    print(f"C2=K*M mod (q)")
    C2=mod((K*M),q)
    return (C1,C2)
def ElgamalDecrypt(C1,C2,q,X):
    K=mod((C1**X),q)
    print(f"K=C1^x mod (q) = {K}")
    Kinv=Extended_Euclidean_quiet(q,K)
    print(f"K-1 mod (q)= {Kinv}")
    print("M=C2*Kinv mod(q)")
    M=mod(C2*Kinv,q)
    return M

def Elgamal():
    q=int(input("Enter q: "))
    choice=int(input("Enter 0 to encrypt, 1 to decrypt, 2 to do both: "))
    if(choice==0):
        a=int(input("Enter value of a: "))
        Y=int(input("Enter public key if given, else enter 0: "))
        if(Y==0):
            X=int(input("Enter private key (x)(<q-1): "))
            Y=public_key_calculation(X,q,a)
            print(f"Public key y= a^x mod(q)={Y}")
        k=int(input("Enter k(>=1)(<=q-1) : "))
        M=int(input("Enter message (>=0)(<=q-1): "))
        (C1,C2)=ElGamalEncrypt(Y,q,a,M,k)
        print(f"(C1,C2)={(C1,C2)}")
    elif(choice==1):
        C1=int(input("Enter C1 value: "))
        C2= int(input("Enter C2 value: "))
        X=int(input("Enter private key (x)(<q-1): "))
        M=ElgamalDecrypt(C1,C2,q,X)
        print(f"M={M}")
    elif(choice==2):
        a=int(input("Enter value of a: "))
        Y=int(input("Enter public key if given, else enter 0: "))
        if(Y==0):
            X=int(input("Enter private key (x)(<q-1): "))
            Y=public_key_calculation(X,q,a)
            print(f"Public key y= a^x mod(q)={Y}")
        else:
            X=int(input("Enter private key (x)(<q-1): "))
        k=int(input("Enter k(>=1)(<=q-1) : "))
        M=int(input("Enter message (>=0)(<=q-1): "))
        (C1,C2)=ElGamalEncrypt(Y,q,a,M,k)
        print(f"(C1,C2)={(C1,C2)}")
        M=ElgamalDecrypt(C1,C2,q,X)
        print(f"M={M}")

