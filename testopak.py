                            #HLAVNÍ SEKCE KÓDU!!!!!!!!!!!!!!(NESMÍ BÝT ROVNO NEBO MENŠÍ NULE,F,PHI,R a OŠETŘENÍ)
def vypocet(F, Phi, R):
   if F != 'x' and float(F) <= 0:
       
       return "F musí být kladné číslo."
   if Phi != 'x' and float(Phi) <= 0:
       
       return "Φ musí být kladné číslo."
   if R != 'x' and float(R) <= 0:
       
       return "R musí být kladné číslo."
   if F == 'x' and Phi != 'x' and R != 'x':
       
       return f"F = {float(Phi) * float(R)} At"
   elif Phi == 'x' and F != 'x' and R != 'x':
       
       return f"Φ = {float(F) / float(R)} Wb"
   elif R == 'x' and F != 'x' and Phi != 'x':
       
       return f"R = {float(F) / float(Phi)} At/Wb"
   return "Nesprávné hodnoty nebo příliš mnoho neznámých."
                                #OPAKOVÁNÍ!!!!!!!!!!!!!!!!!!!
while True:
   
   F = input("Zadejte F nebo 'x' pro neznámé (nebo 'konec' pro ukončení): ")
   if F.lower() == 'konec':
       break
   Phi = input("Zadejte Φ nebo 'x' pro neznámé: ")
   if Phi.lower() == 'konec':
       break
   R = input("Zadejte R nebo 'x' pro neznámé: ")
   if R.lower() == 'konec':
       break
   print(vypocet(F, Phi, R))                   #KÓD VYPÍŠE UŽIVATELI VÝPOČET