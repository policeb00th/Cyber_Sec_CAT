from Euclidean_GCD import Extended_Euclidean_quiet
import math


def mod(a, b):
    if a % b == 0:
        return 0
    if(a > 0):
        return(abs(a) % abs(b))
    else:
        return(abs(b)-(abs(a) % abs(b)))


def AddPoints(P, Q, a, n):
    if(P == Q):
        num = ((3*P[0]*P[0])+a)
        denom = 2*P[1]
        print(f"lambda=3Xp^2+a/2Yp=3*{P[0]}^2 + {a}/2*{P[1]}")
        print(
            f"lambda=3*{P[0]**2}+{a}/{denom}={num}/{denom}= {num} * {denom}^-1 mod({n})")
        lamb = num*Extended_Euclidean_quiet(n, denom)
        print(
            f"lambda={num}*{Extended_Euclidean_quiet(n,denom)}= {lamb} mod({n})")
        lamb = mod(lamb, n)
        print(f"lambda = {lamb}")
    else:
        num = Q[1]-P[1]
        denom = Q[0]-P[0]
        if(denom < 0):
            num *= -1
            denom *= -1
        lamb = num*Extended_Euclidean_quiet(n, denom)
        print(
            f"lambda=(Yp-Yq)/(Xp-Xq)\n\t={Q[1]}-{P[1]}/{Q[0]}-{P[0]}\n\t={num}/{denom} mod({n})\n\t={num}*{denom}^-1 mod({n})")
        print(f"lambda={num}*{Extended_Euclidean_quiet(n,denom)} mod({n})")
        lamb = mod(lamb, n)
        print(f"=>lambda={lamb}")

    xr = lamb**2-P[0]-Q[0]
    yr = lamb*(P[0]-mod(xr, n))-P[1]
    print(
        f"xr=lambda^2- Xp-Xq\n\t={lamb}^2 -{P[0]}-{Q[0]}\n\t={lamb**2}-{P[0]}-{Q[0]}\n\t={xr} mod({n})\n=>xr {mod(xr,n)}")
    print(
        f"yr=lambda * (Xp-xr) -Yp\n\t= {lamb} * ({P[0]}-{mod(xr,n)})-{P[1]}\n\t={yr} mod({n}) \n=>yr={mod(yr,n)}")
    xr, yr = mod(xr, n), mod(yr, n)

    return(xr, yr)


def MultiplyPoints(N, P, a, n):
    arr = [0]*(N+1)
    arr[0] = 0
    arr[1] = P
    for i in range(math.floor((N-1)/2)):
        arr[i+2] = AddPoints(arr[i+1], P, a, n)
        print(
            f"--------------------------------------------------\n{i+2}P={arr[i+1]}+{P}={arr[i+2]} (Calculations above)\n--------------------------------------------------")
    if(N % 2 == 0):
        print(
            f"--------------------------------------------------\n{N}P={N/2}P+{N/2}P={arr[math.floor((N-1)/2)+1]}+{arr[math.floor((N-1)/2)+1]} (Calculations below)\n--------------------------------------------------")
        A = AddPoints(arr[math.floor((N-1)/2)+1],
                      arr[math.floor((N-1)/2)+1], a, n)
    else:
        print(
            f"--------------------------------------------------\n{N}P={(N-1)/2}P+{((N-1)/2)+1}P={arr[math.floor((N-1)/2)]}+{arr[math.floor((N-1)/2)+1]} (Calculations below)\n--------------------------------------------------")
        A = AddPoints(arr[math.floor((N-1)/2)],
                      arr[math.floor((N-1)/2)+1], a, n)

    return A


def SubtractPoints(P, Q, a, n):
    print(f"(Xp,Yp)-(Xq,Yq)=(Xp,Yp)+(Xq,-Yq)  mod n")
    print(f"\t={P}+({Q[0]},-{Q[1]} mod {n})\n={P}+({Q[0]},{mod(n,-Q[1])})")
    print("\n\n")
    A = AddPoints(P, (Q[0], mod(-Q[1], n)), a, n)
    return A


def ECCEncrypt(e1, e2, P, r, a, n):
    print("C1=r*e1 (Calculations below)")
    C1 = MultiplyPoints(r, e1, a, n)
    print(f"C1={C1}")
    print("C2=Plaintext+ r*e2 (Calculations below)\n\t r*e2 caluclations below")
    temp = MultiplyPoints(r, e2, a, n)
    print(f"r*e2={temp}\n C2= {P}+{temp} (Calculations below)")
    C2 = AddPoints(P, temp, a, n)
    print(f"C2={C2}")
    return C1, C2


def ECCDecrypt(C1, C2, d, a, n):
    print("Plaintext= C2- (d*C1)\nCalculating d*C1 below first")
    temp = MultiplyPoints(d, C1, a, n)
    print(f"C1*r={temp}")
    print("C2- {temp} calculation below")
    P = SubtractPoints(C2, temp, a, n)
    return P


def ECC():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    n = int(input("Enter n: "))
    d = int(input("Enter d (enter 0 if not given): "))
    choice = int(input("Enter 0 to encrypt, 1 to decrypt, 2 to do both: "))
    if(choice == 0):
        e1x = int(input("Enter x value of e1: "))
        e1y = int(input("Enter y value of e1: "))
        e1 = (e1x, e1y)
        r = int(input("Enter r value: "))
        if d != 0:
            print(f"e2=d*e1={d}*{e1} (Calculations below)")
            e2 = MultiplyPoints(d, e1, a, n)
        else:
            e2x = int(input("Enter x value of e2: "))
            e2y = int(input("Enter y value of e2: "))
            e2 = (e2x, e2y)

        Px = int(input("Enter x value of plaintext point: "))
        Py = int(input("Enter y value of plaintext point: "))
        P = (Px, Py)
        C1, C2 = ECCEncrypt(e1, e2, P, r, a, n)
        print(f"C1={C1},C2={C2}")
    elif(choice == 1):
        C1x = int(input("Enter x value of C1: "))
        C1y = int(input("Enter y value of C1: "))
        C2x = int(input("Enter x value of C2: "))
        C2y = int(input("Enter y value of C2: "))
        C1 = (C1x, C1y)
        C2 = (C2x, C2y)
        P = ECCDecrypt(C1, C2, d, a, n)
        print(f"Plaintext={P}")
    elif(choice == 2):
        e1x = int(input("Enter x value of e1: "))
        e1y = int(input("Enter y value of e1: "))
        e1 = (e1x, e1y)
        r = int(input("Enter r value: "))
        if d != 0:
            print(f"e2=d*e1={d}*{e1} (Calculations below)")
            e2 = MultiplyPoints(d, e1, a, n)
            print(f"e2={d}*{e1}={e2}")
        else:
            e2x = int(input("Enter x value of e2: "))
            e2y = int(input("Enter y value of e2: "))
            e2 = (e2x, e2y)

        Px = int(input("Enter x value of plaintext point: "))
        Py = int(input("Enter y value of plaintext point: "))
        P = (Px, Py)
        C1, C2 = ECCEncrypt(e1, e2, P, r, a, n)
        print(f"C1={C1},C2={C2}")
        P = ECCDecrypt(C1, C2, d, a, n)
        print(f"Plaintext={P}")

