import sys

try:
    # create new file with x
    
    fhandle = open("test.txt")
except:
    print("couldn't open file")


# write stuff into
data = ["first line\n","second line\n", str(12/4)]
file.writelines(data)




# close that fucking thing
file.close()