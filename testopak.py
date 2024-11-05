                            # VSTUPY
F = input("Magnetomotorická síla (F), zadejte 'x' pokud neznámé: ")
Phi = input("Magnetický tok (Φ), zadejte 'x' pokud neznámé: ")
R = input("Reluktance (𝓡), zadejte 'x' pokud neznámé: ")
                            # PODMÍNKY A NÁSLEDNÝ VÝLEDEK
if F == 'x':
   F = float(Phi) * float(R)
   print(f"Magnetomotorická síla (F) = {F} At")
elif Phi == 'x':
   Phi = float(F) / float(R)
   print(f"Magnetický tok (Φ) = {Phi} Wb")
elif R == 'x':
   R = float(F) / float(Phi)
   print(f"Reluktance (𝓡) = {R} At/Wb")
   