valmax=int(0)
valmin=int(0)
diff=int(0)
num1= int(input("Inserisci primo numero:"))
num2= int(input("Inserisci secondo numero: "))

somma= num1+num2
prod=num1*num2
media=(float((num1+num2)/2))
if(num1>=num2):
    valmax=num1
    valmin=num2
else:
    valmax=num1
    valmin=num2

diff=int(0)
diff=num1-num2

if(diff<0):
    diff=diff*(-1)
    
print("somma: "+str(somma)+ "\nprodotta: "+str(prod)+ "\nmedia"+ str(media)+ "Massimo: "+str(valmax)+ "Minimo: "+str(valmin)+ "Differenza Assoluta: "+str(diff))

