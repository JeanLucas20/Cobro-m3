print()
print()

# input

a= input("Ingrese el número de metros cubicos gastados: ")
luk= int(a)
print()
a1= 10000

# processing

if luk<=50:
    r= print("Los primeros 50 m^3 son gratis, el total a pagar son: "+ str(a1))
    # output

    
else:
    if luk<50 or luk<200:
        b= ((luk-50) * 2000) + a1
        c= round(b, )
        r= print("El costo de agua es: $" + str(c)) # output

if luk>200:
    b= ((luk - 200) * 3000 ) + 310000
    c= round(b, )
    r= print("El costo de venta del producto es: $"+str(c)) # output