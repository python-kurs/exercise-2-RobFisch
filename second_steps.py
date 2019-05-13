# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]
sat_database["GOES"] = 2000
sat_database["WORLDVIEW"] = 0.31
print("I have the following satellites in my database:")

# 2) print out all satellite names contained in the dictionary [2P]
print(sat_database.keys())
# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]
y = input("Von welchem satelliten möchtest du die Auflösung wissen? (Bitte in Großbuchstaben)")
if y == "METEOSAT":
    print("METEOSAT hat eine Auflösung von 3000 Metern.")
elif y == "LANDSAT":
    print("LANDSAT hat eine Auflösung von 30 Metern.")
elif y == "MODIS":
    print("MODIS hat eine Auflösung von 500 Metern.")
elif y == "GOES":
    print("GOES hat eine Auflösung von 2000 Metern.")
elif y == "WORLDVIEW":
    print("WORLDVIEW hat eine Auflösung von 0.31 Metern.")
else:
    print("Ich habe dich leider nicht verstanden.")

#sat_database
#
#for key,val in sat_database:
#    x = input("Von welchem Satelliten möchtest du die Auflösung erfahren?")
#    if x =0 (sat_database.keys())
#    print(sat_database.values)
#print("Die Auflösung von {} ist {} Meter.".format(val, key))
# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

if y in sat_database:
    print("Der Satellit befindet sich im Datensatz.")
else:
    print("Der Satellit befindet sich nicht im Datensatz.")

# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 
Aufl = (sat_database.get(y))
if y in sat_database:
    print("Der wunderschöne Satellit {} besitzt eine tolle Auflösung von {} Metern".format(y,Aufl))
else:
    print("Es gibt nichts zu sagen.")