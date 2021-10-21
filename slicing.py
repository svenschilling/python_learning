# SLICING : UP TO BUT NOT INCLUDING!!!!!
tupel = ("red","blue","green")
liste = ["red","blue","green","black","pink"]
liste2 = ["eins","zwei","drei","vier","fünf","sechs","sieben","acht"]
string = "this is a test string"

newTupel = tupel[0:2]
newListe = liste[2:]
newString = string[-8:-5]
newListe2 = liste2[1:8:2]
newString2 = string[::2]

print(newString2)
print(newListe2)
print(newTupel)
print(newListe)
print(newString)
