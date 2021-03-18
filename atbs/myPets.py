myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a name.')
name = input()
if name not in myPets:
    print(f" I do not have a pet name {name}.")
else:
    print(f"{name} is my pet.")