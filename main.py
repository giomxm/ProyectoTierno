import pandas as pd
import seaborn as sns
datos = pd.read_csv('bebidas.csv')
print("PRIMERAS 5 COMPRAS")
print(datos[0:5], end="\n-----------------------------------------\n")
print("ULTIMAS 5 COMPRAS")
print(datos[995:1000], end="\n-----------------------------------------\n")
lista1 = []
lista2 = []
lista3 = []
lista4 = []
evidencia = []
vero = []
cMenor = 0
cAdulto = 0
cMayor = 0
cFrio = 0
cTemplado = 0
cCalido = 0
cFria = 0
cCaliente = 0

lista1 = datos['Indice']
lista2 = datos['Edad']
lista3 = datos['Temperatura']
lista4 = datos['Bebida']
listaEdad = []
listaTemp = []
listaBebida = []

#Actualizacion tabla edad
for i in range(1000):
    if lista2[i] < 18:
        listaEdad.append("Menor")
    else:
        if lista2[i] >= 18 and lista2[i] < 60:
            listaEdad.append("Adulto")
        else:
            listaEdad.append("Mayor")
            
#Actualizacion tabla temperatura
for j in range(1000):
    if lista3[j] <= 10:
        listaTemp.append("Frio      ")
    else:
        if lista3[j] > 10 and lista3[j] < 20:
            listaTemp.append("Templado")
        else:
                listaTemp.append("Calido   ")  
                
#Actualizacion tabla
for k in range(1000):
    if lista4[k] == 0:
        listaBebida.append("Fria")
    else:
        listaBebida.append("Caliente")
    
nuevaTabla = [lista1, listaEdad, listaTemp, listaBebida]
print("NUEVA TABLA")
print("Indice", end="\t")
print("Edad", end="\t")
print("Temperatura", end="\t      ")
print("Bebida", end="\t\n")

for j in range(5):
    for i in range(4):
        print(nuevaTabla[i][j], end="\t")
    print()
print(end="\n-----------------------------------------\n")
for j in range(995,1000):
    for i in range(4):
        print(nuevaTabla[i][j], end="\t")
    print()
            
df = pd.DataFrame(datos)
sns.lmplot(x='Edad',y='Temperatura', data=df, fit_reg=False,hue='Bebida',
           legend=False, palette='deep')

for i in range(1000):
    if listaEdad[i] == 'Menor':
        cMenor+=1
    else:
        if listaEdad[i] == 'Adulto':
            cAdulto+=1
        else:
            cMayor+=1

cMenor /= 1000 
cAdulto /= 1000 
cMayor /= 1000 
            
print("\n-----------------------------------------\n")
print("Distribucion de probabilidad x")
print("x = Menor:\t",cMenor)
print("x = Adulto:\t",cAdulto)
print("x = Mayor:\t", cMayor)

for i in range(1000):
    if listaTemp[i] == "Frio      ":
        cFrio += 1
    else:
        if listaTemp[i] == 'Templado':
            cTemplado += 1
        else:
            cCalido += 1
cFrio /= 1000
cTemplado /= 1000 
cCalido  /= 1000 

print("\n-----------------------------------------\n")
print("Distribucion de probabilidad y")
print("y = Frio:\t",cFrio)
print("y = Templado:\t", cTemplado)
print("y = Calido:\t", cCalido)


for i in range(1000):
    if listaBebida[i] == 'Fria':
        cFria += 1
    else:
        cCaliente += 1
        
cFria /= 1000 
cCaliente /= 1000
print("\n-----------------------------------------\n")
print("Distribucion de probabilidad z")
print("z = Fria:\t",cFria)
print("z = Caliente:\t",cCaliente)
print("\n-----------------------------------------\n")

print("X = x \t\t Y = y \t\t P(X=x, Y=y)" )
aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Menor" and listaTemp[i] == "Frio      ":
        aux1 += 1
aux1 /= 1000
evidencia.append(aux1)
print("X = menor \t Y = frio \t P(X=menor, Y=frio) = \t",evidencia[0])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Menor" and listaTemp[i] == "Templado":
        aux1 += 1
aux1 /= 1000
evidencia.append(aux1)
print("X = menor \t Y = templado \t P(X=menor, Y=templado) =",evidencia[1])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Menor" and listaTemp[i] == "Calido   ":
        aux1 += 1
aux1 /= 1000
evidencia.append(aux1)
print("X = menor \t Y = calido \t P(X=menor, Y=calido) =",evidencia[2], end="\n")
print()

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Adulto" and listaTemp[i] == "Frio      ":
        aux1 += 1
aux1 /= 1000
evidencia.append(aux1)
print("X = aulto \t Y = frio \t P(X=adulto, Y=frio) = \t",evidencia[3])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Adulto" and listaTemp[i] == "Templado":
        aux1 += 1
aux1 /= 1000
evidencia.append(aux1)
print("X = adulto \t Y = templado \t P(X=adulto, Y=templado) = ",evidencia[4])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Adulto" and listaTemp[i] == "Calido   ":
        aux1 += 1
aux1 /= 1000
evidencia.append(aux1)
print("X = adulto \t Y = calido \t P(X=adulto, Y=calido) = ",evidencia[5],end="\n")
print()

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Mayor" and listaTemp[i] == "Frio      ":
        aux1 += 1
aux1 /= 1000
evidencia.append(aux1)
print("X = mayor \t Y = frio \t P(X=mayor, Y=frio) = \t",evidencia[6])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Mayor" and listaTemp[i] == "Templado":
        aux1 += 1
aux1 /= 1000
evidencia.append(aux1)
print("X = mayor \t Y = templado \t P(X=mayor, Y=templado) = ",evidencia[7])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Mayor" and listaTemp[i] == "Calido   ":
        aux1 += 1
aux1 /= 1000
evidencia.append(aux1)
print("X = mayor \t Y = calido \t P(X=mayor, Y=calido) = ",evidencia[8],end="\n")
print("\n-----------------------------------------\n")

print("X=x \t Y=y \t\t Z=z \t\tP(X=x, Y=y |Z=z)")

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Menor" and listaTemp[i] == "Frio      " and listaBebida[i] == "Fria":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=menor  Y=frio  \t Z=fría  \tP(X=menor, Y=frio |Z=fria) = ",vero[0])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Menor" and listaTemp[i] == "Frio      " and listaBebida[i] == "Caliente":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=menor  Y=frio  \t Z=caliente  \tP(X=menor, Y=frio |Z=caliente) = ",vero[1])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Menor" and listaTemp[i] == "Templado" and listaBebida[i] == "Fria":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=menor  Y=templado  \t Z=Fria  \tP(X=menor, Y=templado |Z=fria) = ",vero[2])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Menor" and listaTemp[i] == "Templado" and listaBebida[i] == "Caliente":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=menor  Y=templado  \t Z=Caliente  \tP(X=menor, Y=templado |Z=Caliente) = ",vero[3])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Menor" and listaTemp[i] == "Calido   " and listaBebida[i] == "Fria":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=menor  Y=calido  \t Z=Fria  \tP(X=menor, Y=calido |Z=fria) = ",vero[4])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Menor" and listaTemp[i] == "Calido   " and listaBebida[i] == "Caliente":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=menor  Y=calido  \t Z=Caliente  \tP(X=menor, Y=templado |Z=Caliente) = ",vero[5])
print() 
#empiezan adultos

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Adulto" and listaTemp[i] == "Frio      " and listaBebida[i] == "Fria":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=adulto  Y=frio  \t Z=fría  \tP(X=adulto, Y=frio |Z=fria) = ",vero[6])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Adulto" and listaTemp[i] == "Frio      " and listaBebida[i] == "Caliente":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=adulto  Y=frio  \t Z=caliente  \tP(X=adulto, Y=frio |Z=caliente) = ",vero[7])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Adulto" and listaTemp[i] == "Templado" and listaBebida[i] == "Fria":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=adulto  Y=templado  \t Z=Fria  \tP(X=adulto, Y=templado |Z=fria) = ",vero[8])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Adulto" and listaTemp[i] == "Templado" and listaBebida[i] == "Caliente":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=adulto  Y=templado  \t Z=Caliente  \tP(X=adulto, Y=templado |Z=Caliente) = ",vero[9])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Adulto" and listaTemp[i] == "Calido   " and listaBebida[i] == "Fria":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=adulto  Y=calido  \t Z=Fria  \tP(X=adulto, Y=calido |Z=fria) = ",vero[10])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Adulto" and listaTemp[i] == "Calido   " and listaBebida[i] == "Caliente":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=adulto  Y=calido  \t Z=Caliente  \tP(X=adulto, Y=templado |Z=Caliente) = ",vero[11])
print()
#empiezan mayores

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Mayor" and listaTemp[i] == "Frio      " and listaBebida[i] == "Fria":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=mayor  Y=frio  \t Z=fría  \tP(X=mayor, Y=frio |Z=fria) = ",vero[12])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Mayor" and listaTemp[i] == "Frio      " and listaBebida[i] == "Caliente":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=mayor  Y=frio  \t Z=caliente  \tP(X=mayor, Y=frio |Z=caliente) = ",vero[13])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Mayor" and listaTemp[i] == "Templado" and listaBebida[i] == "Fria":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=mayor  Y=templado  \t Z=Fria  \tP(X=mayor, Y=templado |Z=fria) = ",vero[14])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Mayor" and listaTemp[i] == "Templado" and listaBebida[i] == "Caliente":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=menor  Y=templado  \t Z=Caliente  \tP(X=mayor, Y=templado |Z=Caliente) = ",vero[15])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Mayor" and listaTemp[i] == "Calido   " and listaBebida[i] == "Fria":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=mayor  Y=calido  \t Z=Fria  \tP(X=mayor, Y=calido |Z=fria) = ",vero[16])

aux1 = 0
for i in range(1000):
    if listaEdad[i] == "Mayor" and listaTemp[i] == "Calido   " and listaBebida[i] == "Caliente":
        aux1 += 1
aux1 /= 1000
vero.append(aux1)
print("X=mayor  Y=calido  \t Z=Caliente  \tP(X=mayor, Y=templado |Z=Caliente) = ",vero[17])

print("\n-----------------------------------------\n")

print("Nuevo Cliente")
clienteEdad = input("Edad: ")
clienteTemp = input("Temperatura del dia: ")

#menor - frio
if clienteEdad == "menor" and clienteTemp == "frio":
    auxFrio = (cFria * vero[0]) / evidencia[0]
    auxCaliente = (cCaliente * vero[1]) / evidencia[0]
    if auxFrio > auxCaliente:
        print("La sugerencia es una bebida fria")
    else:
        print("La sugerencia es una bebida caliente")

#menor - templado
if clienteEdad == "menor" and clienteTemp == "templado":
    auxFrio = (cFria * vero[2]) / evidencia[1]
    auxCaliente = (cCaliente * vero[3]) / evidencia[1]
    if auxFrio > auxCaliente:
        print("La sugerencia es una bebida fria")
    else:
        print("La sugerencia es una bebida caliente")

#menor - calido
if clienteEdad == "menor" and clienteTemp == "calido":
    auxFrio = (cFria * vero[4]) / evidencia[2]
    auxCaliente = (cCaliente * vero[5]) / evidencia[2]
    if auxFrio > auxCaliente:
        print("La sugerencia es una bebida fria")
    else:
        print("La sugerencia es una bebida caliente")


#adulto - frio
if clienteEdad == "adulto" and clienteTemp == "frio":
    auxFrio = (cFria * vero[6]) / evidencia[3]
    auxCaliente = (cCaliente * vero[7]) / evidencia[3]
    if auxFrio > auxCaliente:
        print("La sugerencia es una bebida fria")
    else:
        print("La sugerencia es una bebida caliente")

#adulto - templado
if clienteEdad == "adulto" and clienteTemp == "templado":
    auxFrio = (cFria * vero[8]) / evidencia[4]
    auxCaliente = (cCaliente * vero[9]) / evidencia[4]
    if auxFrio > auxCaliente:
        print("La sugerencia es una bebida fria")
    else:
        print("La sugerencia es una bebida caliente")

        
#adulto - calido
if clienteEdad == "adulto" and clienteTemp == "calido":
    auxFrio = (cFria * vero[10]) / evidencia[5]
    auxCaliente = (cCaliente * vero[11]) / evidencia[5]
    if auxFrio > auxCaliente:
        print("La sugerencia es una bebida fria")
    else:
        print("La sugerencia es una bebida caliente")

#mayor - frio
if clienteEdad == "mayor" and clienteTemp == "frio":
    auxFrio = (cFria * vero[12]) / evidencia[6]
    auxCaliente = (cCaliente * vero[13]) / evidencia[6]
    if auxFrio > auxCaliente:
        print("La sugerencia es una bebida fria")
    else:
        print("La sugerencia es una bebida caliente")

#mayor - templado
if clienteEdad == "mayor" and clienteTemp == "templado":
    auxFrio = (cFria * vero[14]) / evidencia[7]
    auxCaliente = (cCaliente * vero[15]) / evidencia[7]
    if auxFrio > auxCaliente:
        print("La sugerencia es una bebida fria")
    else:
        print("La sugerencia es una bebida caliente")
        
#mayor - calido
if clienteEdad == "mayor" and clienteTemp == "calido":
    auxFrio = (cFria * vero[16]) / evidencia[8]
    auxCaliente = (cCaliente * vero[17]) / evidencia[8]
    if auxFrio > auxCaliente:
        print("La sugerencia es una bebida fria")
    else:
        print("La sugerencia es una bebida caliente")
        
