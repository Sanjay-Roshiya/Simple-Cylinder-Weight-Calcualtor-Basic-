a = float(input("Rod Diameter: "))
b = float(input("Length of Rod :"))
c = float(input("density gm/cm^3 :"))
volume = (22/7)*((a/2)**2)*b
print("Volume = ", volume, "mm^3")
print("Weight = ", (volume*(c/10**6)/1000), "Grams", "or",(volume*(c/10**6)), "Kgs")
