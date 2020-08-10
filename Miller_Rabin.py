def Miller_Rabin(number,a):
    k=0
    m=number-1
    condition=True
    while(condition==True):
        if(m%2==0):
            k+=1
            m/=2
        else:
            condition=False
    print(f"n-1={number-1}={m}*2^{k}")
    print(f"Initialization: T= {a}^{m} mod {number}={(a**m)%number}")
    T=(a**m)%number
    if(abs(T)==1):
        return "Prime"
    for i in range(0,k-1):
        print(f"K={i+1}\tT=T^2 mod n = {T}^2 mod {number}={(T**2)%number}")
        T=(T**2)%number
        if(T==-1):
            return "Prime"
        elif (T==1):
            return "Composite"
    return "Composite"

