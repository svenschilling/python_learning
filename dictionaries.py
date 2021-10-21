gammelfleisch = {"döner" : "ja", "bratwurst" : "ja", "speck" : "nein"}
print(gammelfleisch)
print(gammelfleisch["döner"])

indexTest = {"thursday" : 4, "monday" : 1, "friday" : 5}
print(indexTest)

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 1

print(purse)

purse['candy'] = purse['candy'] + 20

print(purse)

newDict = dict()
names = ['uschi','paula','petra','sandra','katharina','uschi']
for name in names:
    if name not in newDict:
        newDict[name] = 1
    else:
        newDict[name] += 1

print(newDict)

getDict = dict()
test = getDict.get('sven',0)
print(getDict)

d = dict()
d['uschi'] = 10
d['berta'] = 20
d['sandra'] = 30
for (x,y) in d.items():
    print(x,y)