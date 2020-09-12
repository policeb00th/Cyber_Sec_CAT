from math import floor
def Euclidean_GCD(a,b):
    while b!=0:
        print(a,"=",floor(a/b),"x",b,"+",a%b)
        a,b=b,a%b
    return(a)

def Euclidean_GCD_quiet(a,b):
    while b!=0:
        a,b=b,a%b
    return(a)
def Extended_Euclidean(domain,value):
    if(Euclidean_GCD(domain,value)==1):
        print("q\tr1\tr2\tr\tt1\tt2\tt")
        t1,t2,r1,r2=0,1,domain,value
        while r2!=0:
            q=floor(r1/r2)
            r=r1%r2
            t=t1-q*t2
            print(q,"\t",r1,"\t",r2,"\t",r,"\t",t1,"\t",t2,"\t",t)
            r1,r2,t1,t2=r2,r,t2,t
        if(t1<0):
            print("Negative modulo is:",t1)
            while t1<0:
                t1+=domain
        return(t1)
    else:
        return("No inverse exists")

def Extended_Euclidean_quiet(domain,value):
    if(Euclidean_GCD_quiet(domain,value)==1):
        t1,t2,r1,r2=0,1,domain,value
        while r2!=0:
            q=floor(r1/r2)
            r=r1%r2
            t=t1-q*t2
            r1,r2,t1,t2=r2,r,t2,t
        if(t1<0):
            while t1<0:
                t1+=domain
        return(t1)
    else:
        return("No inverse exists")