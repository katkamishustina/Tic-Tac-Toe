import numpy
import matplotlib

sequence = input("Write a sequence:")
complement = ''
for a in range(len(sequence)):
    if sequence[a] == "A":
        complement += "T"
    elif sequence[a] == "T":
        complement += "A"
    elif sequence[a] == "C":
        complement += "G"
    elif sequence[a] == "G":
        complement += "C"
    elif sequence[a] == "R":
        complement += "Y"
    elif sequence[a] == "Y":
        complement += "R"
    elif sequence[a] == "M":
        complement += "K"
    elif sequence[a] == "K":
        complement += "M"
    elif sequence[a] == "H":
        complement += "D"
    elif sequence[a] == "D":
        complement += "H"
    elif sequence[a] == "B":
        complement += "V"
    elif sequence[a] == "V":
        complement += "B"
    elif sequence[a] == " ":
        complement += " "


print('sequence:   ' + sequence)
print('complement: ' + complement)




