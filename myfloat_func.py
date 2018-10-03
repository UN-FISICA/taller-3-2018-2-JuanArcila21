def suma(c,d):
    a=[c[0][:],c[1][:]]
    b=[d[0][:],d[1][:]]
    if min(len(a[1]),len(b[1]))==len(a[1]):
        for i in range(len(b[1])-len(a[1])):
            a[1].append(0)
    if min(len(a[1]),len(b[1]))==len(b[1]):
        for i in range(len(a[1])-len(b[1])):
            b[1].append(0)
    if min(len(a[0]),len(b[0]))==len(a[0]):
        for i in range(len(b[0])-len(a[0])):
            a[0].insert(1,0)
    if min(len(a[0]),len(b[0]))==len(b[0]):
        for i in range(len(a[0])-len(b[0])):
            b[0].insert(1,0)
    resultado=[[],[]]
    if a[0][0]=="-":
        a[0][0]="+"
        sumacorregida=resta(b,a)
        resultado[0]=sumacorregida[0]
        resultado[1]=sumacorregida[1]
        resultadoentupla=(resultado[0],resultado[1])
        a[0][0]="-"
        return resultadoentupla
    elif b[0][0]=="-":
        b[0][0]="+"
        sumacorregida=resta(a,b)
        resultado[0]=sumacorregida[0]
        resultado[1]=sumacorregida[1]
        resultadoentupla=(resultado[0],resultado[1])
        b[0][0]="-"
        return resultadoentupla

    else:
        sobra=0
        for i in range(len(a[1])):
            resultado[1].insert(0,int(str(a[1][-i-1]+b[1][-i-1])[-1])+int(sobra))
            str(a[1][-i-1]+b[1][-i-1])[:-1]
            sobra=str(a[1][-i-1]+b[1][-i-1])[:-1]
            if len(sobra)==0:
                sobra=0
        for i in range(len(a[0])-1):
            resultado[0].insert(0,int(str(a[0][-i-1]+b[0][-i-1])[-1])+int(sobra))
            sobra=str(a[0][-i-1]+b[0][-i-1])[:-1]
            if len(sobra)==0:
                sobra=0
        if type(sobra) is str:
            resultado[0].insert(0,int(sobra))

        resultado[0].insert(0,"+")
        resultadoentupla=(resultado[0],resultado[1])
        return resultadoentupla
def resta(c,d):   
    a=[c[0][:],c[1][:]]
    b=[d[0][:],d[1][:]]
    if min(len(a[1]),len(b[1]))==len(a[1]):
        for i in range(len(b[1])-len(a[1])):
            a[1].append(0)
    if min(len(a[1]),len(b[1]))==len(b[1]):
        for i in range(len(a[1])-len(b[1])):
            b[1].append(0)
    if min(len(a[0]),len(b[0]))==len(a[0]):
        for i in range(len(b[0])-len(a[0])):
            a[0].insert(1,0)
    if min(len(a[0]),len(b[0]))==len(b[0]):
        for i in range(len(a[0])-len(b[0])):
            b[0].insert(1,0)
    resultado=[[],[]]
    if a[0][0]=="-" and b[0][0]=="+":
        a[0][0]="+"
        sumacorregida=suma(a,b) #-a-b=-(a+b)
        sumacorregida[0][0]="-"
        resultado[0]=sumacorregida[0]
        resultado[1]=sumacorregida[1]
        a[0][0]="-"
        
    elif b[0][0]=="-":
        b[0][0]="+"
        sumacorregida=suma(a,b)
        resultado[0]=sumacorregida[0]
        resultado[1]=sumacorregida[1]
        b[0][0]="-"


    else:
        contador3=1
        while contador3<len(c[0]):
            if c[0][contador3]>d[0][contador3]:
                a=[c[0],c[1]]
                b=[d[0],d[1]]
                for i in range(len(a[1])):
                    if a[1][-i-1]<b[1][-i-1]:
                        try:
                            a[1][-i-2]-=1
                            a[1][-i-1]+=10
                            resultado[1].insert(0,int(str(a[1][-i-1]-b[1][-i-1])))
                        except:
                            a[1][-i-1]+=10
                            a[0][len(a[0])-1]-=1
                            resultado[1].insert(0,int(str(a[1][-i-1]-b[1][-i-1])))
                    else:
                        resultado[1].insert(0,int(str(a[1][-i-1]-b[1][-i-1])))
                for i in range(len(a[0])-1):
                    if a[0][-i-1]<b[0][-i-1]:
                        a[0][-i-1]+=10
                        a[0][-i-2]-=1
                        resultado[0].insert(0,int(str(a[0][-i-1]-b[0][-i-1])))
                    else:
                        resultado[0].insert(0,int(str(a[0][-i-1]-b[0][-i-1])))
                resultado[0].insert(0,"+")
                contador3=len(c[0])+20
            else:
                contador3+=1
        if contador3!=len(c[0])+20:
            b=[c[0],c[1]]
            a=[d[0],d[1]]
            for i in range(len(a[1])):
                if a[1][-i-1]<b[1][-i-1]:
                    try:
                        a[1][-i-2]-=1
                        a[1][-i-1]+=10
                        resultado[1].insert(0,int(str(a[1][-i-1]-b[1][-i-1])))
                    except:
                        a[1][-i-1]+=10
                        a[0][len(a[0])-1]-=1
                        resultado[1].insert(0,int(str(a[1][-i-1]-b[1][-i-1])))
                else:
                    resultado[1].insert(0,int(str(a[1][-i-1]-b[1][-i-1])))
            for i in range(len(a[0])-1):
                if a[0][-i-1]<b[0][-i-1] and type(a[0][-i-2]) is int:
                    a[0][-i-2]-=1
                    a[0][-i-1]+=10
                    resultado[0].insert(0,int(str(a[0][-i-1]-b[0][-i-1])))
                else:
                    resultado[0].insert(0,int(str(a[0][-i-1]-b[0][-i-1]))) 
            resultado[0].insert(0,"-")
    resultadoentupla=(resultado[0],resultado[1])
    return resultadoentupla
def division(a,b,decimales=101):
    if (a[0][0]=="-" and b[0][0]=="+") or (a[0][0]=="+" and b[0][0]=="-"):
        signo=0
    else:
        signo=1
    signa=a[0][0]
    signb=b[0][0]
    del a[0][0]
    del b[0][0]
    c=[]
    d=[]
    divdecimal=""
    diventero=""
    for i in range (len(a[0])):
        c.append(a[0][i])
    for j in range (len(a[1])):
        c.append(a[1][j])
    if len(a[1])<len(b[1]):
        cero=len(b[1])-len(a[1])
        for k in range(cero):
            c.append(0)
    for l in range(len(b[0])):
        d.append(b[0][l])
    for m in range (len(b[1])):
        d.append(b[1][m])
    if len(b[1])<len(a[1]):
        cero=len(a[1])-len(b[1])
        for k in range(cero):
            d.append(0)
    num1=float("".join(str(n) for n in c))
    num2=float("".join(str(o) for o in d))
    diventero+=str(int(num1/num2))
    mod=(num1%num2)*10
    for p in range (decimales):
        rest=int(mod/num2)
        divdecimal+=str(rest)
        mod=(mod%num2)*10
    a0=list(map(int,diventero))
    a1=list(map(int,divdecimal))
    if signo==0:
        a0.insert(0,"-")
    if signo==1:
        a0.insert(0,"+")
    if decimales==101:
        if num1%num2==0:
            a1=[]
            a1.append(0)
        else:
            q=0
            while q==0:
                if a1[-1]=="0":
                    a1.pop(-1)
                else:
                    q=1
    resultado=(a0,a1)
    a[0].insert(0,signa)
    b[0].insert(0,signb)
    return(resultado)
def multiplicacion(a,b):
    if (a[0][0]=="-" and b[0][0]=="+") or (a[0][0]=="+" and b[0][0]=="-"):
        signo=0
    else:
        signo=1

    c=a[0]+a[1]
    c.pop(0)
    d=b[0]+b[1]
    d.pop(0)
    sobra=0
    resul=[]
    resultado=[]
    ceros=0
    coma=len(a[1])+len(b[1])
    for j in range(len(d)):
        resul.append([])
        if ceros>=1:
            for k in range(ceros):
                resul[j].insert(0,0)
        for i in range (len(c)):
            mul=((c[-i-1]*d[-j-1])+sobra)%10
            sobra=int(((c[-i-1]*d[-j-1])+sobra)/10)
            resul[j].insert(0,mul)
        if (c[0]*d[-j-1])+sobra>9:
            resul[j].insert(0,sobra)        
        ceros+=1
        sobra=0
    for l in range(len(resul)):
        longitud=len(resul[-1])-len(resul[l])
        for m in range(longitud):
            resul[l].insert(0,0)
    suma=0
    lleva=0
    for p in range (len(resul[0])):
        if len(resultado)==len(resul[0])-1:
            resul[0].insert(0,0)
        for n in range (len(resul)):
            suma=resul[n][-p-1]+suma
        if suma>9:
            total=suma%10
            resultado.insert(0,total)
            lleva=int(suma/10)
        else:
            resultado.insert(0,suma)
            lleva=0
        resul[0][-p-2]+=lleva
        suma=0
    if lleva!=0:
        resultado.insert(0,resul[0][0])
    a0=[]
    a1=[]
    for q in range (coma):
        a1.append(resultado[-coma+q])
    for s in range(len(resultado)-coma):
        a0.append(resultado[s])
    for t in range (len(a1)):
        if len(a1)==1:
            break
        else:
            if a1[-1]==0:
                a1.pop(-1)
    if signo==0:
        a0.insert(0,"-")
    else:
        a0.insert(0,"+")
    final=(a0,a1)
    return(final)
def pi():
    uno=(["+",1],[0])
    muno=(["-",1],[0])
    dos=(["+",2],[0])
    cuatro=(["+",4],[0])
    resultado=(["+",0],[0])
    k=0
    while k<10000:
        kfloat=(["+",k],[0])
        denominador=suma(multiplicacion(dos,kfloat),uno)
        if k%2==0:
            resultado=suma(resultado,division(cuatro,denominador))
        else:
            resultado=suma(resultado,multiplicacion(division(cuatro,denominador),muno))
        k+=1
    return resultado
print (pi())
            