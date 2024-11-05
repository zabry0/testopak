def vypocet(F, Phi, R):

    if F == 'x' and Phi != 'x' and R != 'x':

        return f"F = {float(Phi) * float(R)} At"

    elif Phi == 'x' and F != 'x' and R != 'x':

        return f"Φ = {float(F) / float(R)} Wb"

    elif R == 'x' and F != 'x' and Phi != 'x':

        return f"R = {float(F) / float(Phi)} At/Wb"

    return "Nesprávné hodnoty nebo příliš mnoho neznámých."

# VSTUPY

F = input("Zadejte F nebo 'x' pro neznámé: ")
Phi = input("Zadejte Φ nebo 'x' pro neznámé: ")
R = input("Zadejte R nebo 'x' pro neznámé: ")

# VÝPOČET A VYPIS VÝSLEDKU

print(vypocet(F, Phi, R)) 