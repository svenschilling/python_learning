import pickle, sys


class Telefonbuch:
    # anzahl der gesamteintrage im telefonbuch
    eintraege = 0

    def __init__(self,vorname,familienname,telefonnummer):
        self.name = vorname
        self.nachname = familienname
        self.nummer = telefonnummer

# file handling
try:
    file = open("serial.bin", "bw")

except:
    print("couldn't find/open file")
    sys.exit(0)

# object
x = (["test","abc",23], "xyz")
pickle.dump(x,file)


# class object
eintrag = Telefonbuch("sven","schilling","0124232345")
pickle.dump(eintrag,file)


# close file
file.close()




