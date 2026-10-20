Mercurio= 0.38
Venere= 0.91
Terra= 1.00
Marte= 0.38
Giove= 2.34
Saturno= 1.06
Urano= 0.92
Nettuno= 1.19

pesopers= float(input("inserisci il tuo peso: "))
pianeta= input("Scegli pianeta: ")
peso=float(0)

if(pianeta=="Mercurio"):
    peso=pesopers*Mercurio
elif(pianeta=="Venere"):
    peso=pesopers*Venere
elif(pianeta=="Terra"):
    peso=pesopers*Terra
elif(pianeta=="Marte"):
    peso=pesopers*Marte
elif(pianeta=="Giove"):
    peso=pesopers*Giove
elif(pianeta=="Saturno"):
    peso=pesopers*Saturno
elif(pianeta=="Urano"):
    peso=pesopers*Urano
elif(pianeta=="Nettuno"):
    peso=pesopers*Nettuno


print("Sulla terra il tuo peso è "+ str(pesopers) +"Kg, mentre su "+ str(pianeta) +" il tuo peso è "+ str(peso))
