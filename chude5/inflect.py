
import inflect

p = inflect.engine()
names = []

while True:
    name = input("Name: ")
    if name == "":
        break
    names.append(name)

print("Adieu, adieu, to " + p.join(names))
