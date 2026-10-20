x1= float(input("coordinata x del centro della prima circonferenza: "))
y1= float(input("coordinata y del centro della prima circonferenza: "))
r1= float(input("raggio della prima circonferenza: "))
x2= float(input("coordinata x del centro della seconda circonferenza: "))
y2= float(input("coordinata y del centro della seconda circonferenza: "))
r2= float(input("raggio della seconda circonferenza: "))

dist= ((x2-x1)**2 + (y2-y1)**2) **(1/2)

if(dist>r1+r2):
    print("rette esterne")
elif(dist==r1+r2):
    print("Rette esternamente Tangenti")
elif(dist<r1+r2):
    print("Circoferenze secanti")
elif(dist==r1-r2):
    print("Tangenti internamente")
elif(dist<r1-r2 and dist>0):
    print("Circonferenza Interna")
elif(dist==0)
    print("Concentriche")



