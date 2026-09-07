import sys
#OPPGAVE 1
telefonbok = []

person1 = {
   "navn": "mattebassen",
   "nummer": 94823312
}

person2 = {
    "navn": "sverre",
    "nummer": 46576760
}

telefonbok.append(person1)
telefonbok.append(person2)

#OPPGAVE 2
def visAlle():
    for person in telefonbok:
        print(f"Navn: {person["navn"]}, Nummer: {person["nummer"]}")

#OPPGAVE 3
def leggTilPerson():
    print("Legg til en person inn i databasen her")
    
    leggTilNavn = input("Hva er navnet til personen? ")
    leggTilNummer = input("Hva er nummeret til personen? ")
    
    nyPerson = {
        "navn": leggTilNavn,
        "nummer": leggTilNummer
    }
    
    print(f"Informasjon opprettet: Navn: {nyPerson["navn"]}, Nummer: {nyPerson["nummer"]}")
    telefonbok.append(nyPerson)

#OPPGAVE 4
def søk():
    etterlystNavn = input("Søk et navn: ").lower()
    funnet = False
    
    for person in telefonbok:
        if etterlystNavn == person["navn"]:
            print(f"Vi har {etterlystNavn}, Nummer: {person["nummer"]}")
            funnet = True
    
    if not funnet:
        print(f"Vi har ikke personen: {etterlystNavn}")
        
        
#OPPGAVE 5
while True:
    
    print("1. Vis Alle \n2. legg til ny \n3. Søk \n4. Avslutt")
    
    valg = input("Hva vil du gjøre? ").lower()
                
    if valg in ["1", "vis alle"]:
        print("Du valgte: Vis Alle")
        visAlle()
                
    elif valg in ["2", "legg til ny"]:
        print("Du valgte: Legg til ny")
        leggTilPerson()
            
    elif valg in ["3", "søk"]:
            print("Du valgte: søk")
            søk()
    
    elif valg in ["4", "avslutt"]:
            print("Du valgte: Avslutt, programmet avsluttes")
            break

    else:
        print("Ugyldig valg")
