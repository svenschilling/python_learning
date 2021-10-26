import re

string = "hello i'm a super boring string with an emailadress emailadress@superboringcompany.com"

try:
    f = open('regex.txt','r')

except:
    print("fooocking error mate!")

reFind = re.findall('^hell',f.read())

print(reFind)