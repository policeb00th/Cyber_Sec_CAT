import Euclidean_GCD


def CRT(n):
    m, a, z, y, x, w = [], [], [], [], 0, []
    M = 1
    for i in range(n):
        ain = int(input("Enter value: "))
        Min = int(input("enter modulo value: "))
        m.append(Min)
        a.append(ain)
    for i in m:
        M *= i
    print("M=", M)
    for i in range(n):
        print(f"Z{i+1} = M/M{i+1}={M}/{m[i]}={M/m[i]}")
        z.append(M/m[i])
    for i in range(n):
        temp = Euclidean_GCD.Extended_Euclidean(m[i], z[i])
        print(f"y{i+1}=Z{i+1}^-1(mod m{i+1})={temp}")
        y.append(temp)
    for i in range(n):
        print(
            f"w{i+1}=y{i+1}Z{i+1}(mod m)= {y[i]}*{z[i]}(mod {M}) = {(y[i]*z[i])%M}")
        w.append((y[i]*z[i]) % M)
    for i in range(n):
        print(f"a{i+1},w{i+1}={a[i]},{w[i]}")
        x += a[i]*w[i]
    print(f"x=Sigma(AW)(mod m) ={x}(mod {M}) ={x%M}")
