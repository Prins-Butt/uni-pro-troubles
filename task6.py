import math

def calculateVolumeOfCylinder(radius, height):
    return math.pi * math.pow(radius, 2) * height

def calculateVolumeOfCone(radius, height):
    return calculateVolumeOfCylinder(radius, height) / 3

def run():

    structure = input("What structure do you what to calculate the volume of? (cylinder / cone): ")

    if structure != "cylinder" and structure != "cone":
        return print("You have to select either cylinder or cone.")

    radius = float(input("What is the radius? "))
    height = float(input("What is the height? "))

    if structure == "cylinder":
        print("The volume is: " + str(calculateVolumeOfCylinder(radius, height)))
    elif structure == "cone":
        print("The volume is: " + str(calculateVolumeOfCone(radius, height)))

run()
