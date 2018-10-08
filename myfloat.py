def imprimir(a):
    num=""
    for i in range(len(a)):
        for j in range(len(a[i])):
            num+=str(a[i][j])
        if len(num)==len(a[0]):   
            num+=","
    return num

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
    
def comparacion(c,d):
    a=[c[0],c[1]]
    b=[d[0],d[1]]
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
    if a[0]==b[0] and a[1]==b[1]:
        return True
    else:
        return False
        
        
class MyFloat:

    def __init__(self,a):
        self.a=a


    def __add__(self,other):
        if type(other)==int or type(other)==float:
            c=[[],[]]
            if other<0:
                e=other*(-1)
            else:
                e=other
            if type(e)==int:
                c[0]=list(map(int,str(e)))
                c[1].append(0)
            else:
                d=str(e)
                for i in range (d.index(".")):
                    c[0].append(int(d[i]))
                z=len(d)-d.index(".")
                for l in range(z-1):
                    c[1].insert(0,int(d[-l-1]))
                    
            
            if other<0:
                c[0].insert(0,"-")
            else:
                c[0].insert(0,"+")
            return(suma(self.a,c))
        else:
            return(suma(self.a,other.a))

    def __sub__(self,other):
        if type(other)==int or type(other)==float:
            c=[[],[]]
            if other<0:
                e=other*(-1)
            else:
                e=other
            if type(e)==int:
                c[0]=list(map(int,str(e)))
                c[1].append(0)
            else:
                d=str(e)
                for i in range (d.index(".")):
                    c[0].append(int(d[i]))
                z=len(d)-d.index(".")
                for l in range(z-1):
                    c[1].insert(0,int(d[-l-1]))
            if other<0:
                c[0].insert(0,"-")
            else:
                c[0].insert(0,"+")
            
            return(resta(self.a,c))
        else:
            return(resta(self.a,other.a))


    def __mul__(self,other):
        
        if type(other)==int or type(other)==float:
            c=[[],[]]
            if other<0:
                e=other*(-1)
            else:
                e=other
            if type(e)==int:
                c[0]=list(map(int,str(e)))
                c[1].append(0)
            else:
                d=str(e)
                for i in range (d.index(".")):
                    c[0].append(int(d[i]))
                z=len(d)-d.index(".")
                for l in range(z-1):
                    c[1].insert(0,int(d[-l-1]))
                    
            
            if other<0:
                c[0].insert(0,"-")
            else:
                c[0].insert(0,"+")
            return(multiplicacion(self.a,c))
        else:
            return(multiplicacion(self.a,other.a))

    def __truediv__(self,other):
        if type(other)==int or type(other)==float:
            c=[[],[]]
            if other<0:
                e=other*(-1)
            else:
                e=other
            if type(e)==int:
                c[0]=list(map(int,str(e)))
                c[1].append(0)
            else:
                d=str(e)
                for i in range (d.index(".")):
                    c[0].append(int(d[i]))
                z=len(d)-d.index(".")
                for l in range(z-1):
                    c[1].insert(0,int(d[-l-1]))
                    
            
            if other<0:
                c[0].insert(0,"-")
            else:
                c[0].insert(0,"+")
            return(division(self.a,c,30))
        else:
            return(division(self.a,other.a,30))

    def __radd__(self,other):
        return (self.__add__(other))

    def __rsub__(self,other):
        if type(other)==int or type(other)==float:
            c=[[],[]]
            if other<0:
                e=other*(-1)
            else:
                e=other
            if type(e)==int:
                c[0]=list(map(int,str(e)))
                c[1].append(0)
            else:
                d=str(e)
                for i in range (d.index(".")):
                    c[0].append(int(d[i]))
                z=len(d)-d.index(".")
                for l in range(z-1):
                    c[1].insert(0,int(d[-l-1]))
            if other<0:
                c[0].insert(0,"-")
            else:
                c[0].insert(0,"+")

            return(resta(c,self.a))
        else:
            return(resta(other.a,self.a))

    def __rmul__(self,other):
        return(self.__mul__(other))

    def __rtruediv__(self,other):
        if type(other)==int or type(other)==float:
            c=[[],[]]
            if other<0:
                e=other*(-1)
            else:
                e=other
            if type(e)==int:
                c[0]=list(map(int,str(e)))
                c[1].append(0)
            else:
                d=str(e)
                for i in range (d.index(".")):
                    c[0].append(int(d[i]))
                z=len(d)-d.index(".")
                for l in range(z-1):
                    c[1].insert(0,int(d[-l-1]))
                    
            
            if other<0:
                c[0].insert(0,"-")
            else:
                c[0].insert(0,"+")
            return(division(c,self.a,30))
        else:
            return(division(other.a,self.a,30))

    def __str__(self):
        pr=""
        if self.a[0][0]=="+":
            pass
        else:
            pr+=str(self.a[0][0])
        for i in range (len(self.a[0])-1):
            pr+=str(self.a[0][i+1])
        pr+=","
        for j in range (len(self.a[1])):
            pr+=str(self.a[1][j])
        return(pr)

    def __repr__(self):
        pr=""
        if self.a[0][0]=="+":
            pass
        else:
            pr+=str(self.a[0][0])
        for i in range (len(self.a[0])-1):
            pr+=str(self.a[0][i+1])
        pr+=","
        for j in range (len(self.a[1])):
            pr+=str(self.a[1][j])
        return (pr)

    def __eq__(self,other):
        if type(other)==int or type(other)==float:
            c=[[],[]]
            if other<0:
                e=other*(-1)
            else:
                e=other
            if type(e)==int:
                c[0]=list(map(int,str(e)))
                c[1].append(0)
            else:
                d=str(e)
                for i in range (d.index(".")):
                    c[0].append(int(d[i]))
                z=len(d)-d.index(".")
                for l in range(z-1):
                    c[1].insert(0,int(d[-l-1]))
                    
            
            if other<0:
                c[0].insert(0,"-")
            else:
                c[0].insert(0,"+")
            return(comparacion(self.a,c))
        else:
            return(comparacion(self.a,other.a))

    def __ne__(self,other):
        if type(other)==int or type(other)==float:
            c=[[],[]]
            if other<0:
                e=other*(-1)
            else:
                e=other
            if type(e)==int:
                c[0]=list(map(int,str(e)))
                c[1].append(0)
            else:
                d=str(e)
                for i in range (d.index(".")):
                    c[0].append(int(d[i]))
                z=len(d)-d.index(".")
                for l in range(z-1):
                    c[1].insert(0,int(d[-l-1]))
                    
            
            if other<0:
                c[0].insert(0,"-")
            else:
                c[0].insert(0,"+")
            condicion=comparacion(c,self.a)
            if condicion==True:
                return(False)
            else:
                return(True)
        else:
            condicion=comparacion(other.a,self.a)
            if condicion==True:
                return(False)
            else:
                return(True)
       
if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
    resultado=0
    k=0
    while k<1000000:
        denominador=2*k+1
        if k%2==0:
            resultado=resultado+(4/denominador)
        else:
            resultado=resultado-(4/denominador)
        k+=1
    print (resultado)
