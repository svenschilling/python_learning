from typing import ClassVar


class Telefonbuch:
    # anzahl der gesamteintrage im telefonbuch
    eintraege = 0

    def __init__(self,vorname,familienname,telefonnummer):
        self.name = vorname
        self.nachname = familienname
        self.nummer = telefonnummer
    
    # destruktor
    def __delattr__(self, name: str) -> None:
        pass
    

    


print(Telefonbuch.eintraege)
        
    
