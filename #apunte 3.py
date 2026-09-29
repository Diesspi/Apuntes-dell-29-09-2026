#apunte 3
print("De cuanto es el total de tu compra?")
comp = int(input())

if comp >= 500000:
    comp = comp * .7
    print(comp)
elif comp >= 400000:
    comp = comp * .75
    print(comp)
elif comp >= 300000:
    comp = comp * .8
    print(comp)
elif comp >= 200000:
    comp = comp * .85
    print(comp)
elif comp >= 100000:
    comp = comp * .9
    print(comp)
else:
    print(comp)