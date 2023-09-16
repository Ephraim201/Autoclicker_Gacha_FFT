import units
import math
import random

personajes = [
    units.Summon_All(1,"AleDriv", "⭐⭐⭐⭐⭐", "GACHA\\AleDriv.png"),
    units.Summon_All(2,"Cloud Blue", "⭐⭐⭐", "GACHA\\CB.png"),
    units.Summon_All(3,"Cloud Red", "⭐⭐⭐", "GACHA\\CG.png"),
    units.Summon_All(4,"Cloud Grenn", "⭐⭐⭐", "GACHA\\CR.png"),
    units.Summon_All(5,"ForkDriv", "⭐⭐⭐⭐⭐", "GACHA\\Fork.png"),
    units.Summon_All(6,"Cloud Nerd", "⭐⭐⭐⭐", "GACHA\\gafasnerd.png"),
    units.Summon_All(7,"Cloud Chad", "⭐⭐⭐⭐", "GACHA\\gafasSol.png"),
    units.Summon_All(8,"Killer Kirbe", "⭐⭐⭐⭐", "GACHA\\KirbyKiller.png"),
    units.Summon_All(9,"Cool Kirbe", "⭐⭐⭐", "GACHA\\KirbyGorra.png")
]


Total_Units = len(personajes)

INV_FIVE = (0.05 * Total_Units) #5%
INV_FOUR = (0.30 * Total_Units) #30%
INV_THREE = (0.65 * Total_Units) #65%

SUMMONED = random.randint(1, len(personajes))

Total = random.randint(1, 100)
print(Total)
if Total <= 5:
    print("5")
    for Summon_All in personajes:
        if Summon_All.stars == "⭐⭐⭐⭐⭐":
            print(Summon_All.stars)

if Total <= 30 and Total >= 6:
    print("4")

if Total >= 30:
    print("3")
    for Summon_All in personajes:
        if Summon_All.stars == "⭐⭐⭐":
            print(Summon_All.stars)

"""
print(SUMMONED)


#Operacion


print(INV_FIVE)
print(INV_FOUR)
print(INV_THREE)


for Summon_All in personajes:
    if Summon_All.stars == "⭐⭐⭐⭐⭐":
        print(Summon_All.stars)

"""