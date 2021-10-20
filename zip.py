plz = ["59034","32052","33062"]
stadt = ["herford","hamm","bielefeld"]
bundesland = ["nrw","sachsen","hessen","bayern"]

# verbindet die elemente der reihenfolge nach
verbunden = zip(plz,stadt,bundesland)


print(verbunden)

# durch iterieren zur ausgabe
for x in verbunden:
    print(x)