temp = input("Hva er tempraturen i farenheit?")

celc = (int(temp) - 32) * (5/9)

celsisus_til_fahrenheit = ((9/5) * int(celc) + 32)


print("tempratur i celsius:" + str(round(celc,1)))
print("tempratur i fahrenheit" + str(round(celsisus_til_fahrenheit,1)))

