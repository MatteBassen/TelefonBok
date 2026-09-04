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
    print(f"Informasjon opprettet: Navn: {nyPerson["navn"]}, Nummer: {nyPerson["nummer"]}")
    
    nyPerson = {
        "navn": leggTilNavn,
        "nummer": leggTilNummer
    }
    
    telefonbok.append(nyPerson)

#OPPGAVE 4
def søk():
    etterlystNavn = input("Søk et navn: ").lower()
    for person in telefonbok:
        if etterlystNavn == person["navn"]:
            print(f"Vi har {etterlystNavn}, Nummer: {person["nummer"]}")
    print(f"Vi har ikke personen: {etterlystNavn}")

#OPPGAVE 5
