print("Gib dein monatliches Gehalt ein: ")
gehalt = int(input())
if gehalt > 2500 and gehalt > 4000:
    steuer = (gehalt/100)*26
    print("Es ergibt sich eine Steuer von: " + str(steuer))
elif gehalt > 2500 and gehalt < 4000:
    steuer = (gehalt/100)*22
    print("Es ergibt sich eine Steuer von: " + str(steuer))
elif gehalt < 2500:
    steuer = (gehalt/100)*18
    print("Es ergibt sich eine Steuer von: " + str(steuer))
else:
    print("WTF hast du eingegeben?")