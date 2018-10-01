print("debut");
a=1
b=1
c=1
d=1
e=1
f=1
g=1
h=8
i=2
while (a<10) :
    if a==h or a==i:
        a=a+1
        continue
    b=1
    while (b<10) :
        
        if b==a or b==i or b==h:
            b=b+1
            continue
        c=1
        while (c<10) :
            
            if c==a or c==b or c ==h or c==i:
                c=c+1
                continue
            d=1
            while (d<10) :
                
                if d==a or d==b or d==c or d==i or d==h:
                    d=d+1
                    continue
                e=1
                while (e<10) :
                    
                    if e==a or e==b or e==c or e==d or e==h or e==i:
                        e=e+1
                        continue
                    f=1
                    while (f<9) :
                        
                        if f==e or f==a or f==b or f==c or f==d or f==i or f==h:
                            f=f+1
                            continue
                        g=1
                        while (g<10) :
                            
                            if g==e or g==a or g==b or g==c or g==d or g==f or g==h or g==i:
                                g=g+1
                                continue
                            if (((((a+13)*b)/c+d+12)*e)-f-11+g)==19:
                                print(a,b,c,d,e,f,g) ;
                                print(((((a+13)*b)/(c+0.0)+d+12)*e)-f-11+g)
                            g=g+1
                        f=f+1
                    e=e+1
                d=d+1
            c=c+1
        b=b+1
    a=a+1;