import pickle,sys

# to load a class obj the same class has to occur inside the deserialisation code as in the serialisation code
class Telefonbuch:
    # anzahl der gesamteintrage im telefonbuch
    eintraege = 0

    def __init__(self,vorname,familienname,telefonnummer):
        self.name = vorname
        self.nachname = familienname
        self.nummer = telefonnummer

    def __str__(self):
        return self.name + "\n" \
            + self.nachname + "\n" \
            + self.nummer + "\n" \

# file handling
try:
    file = open("serial.bin","br")
except:
    print("couldn't open file")
    sys.exit(0)

# object
y = pickle.load(file)
print(y)

# class object
eintraege = pickle.load(file)
print(eintraege)

