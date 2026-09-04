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

def visAlle():
    for person in telefonbok:
        print(f"Navn: {person["navn"]}, Nummer: {person["nummer"]}")

visAlle()