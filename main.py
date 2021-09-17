firstnumber = float(input("Give the value of first point [m - height]: "))
secondnumber = float(input("Give the value of second point [m - height]: "))
distance = float(input("Give the value of the distance on the map [mm - distance on map]: "))
if firstnumber < secondnumber:
    firstnumber, secondnumber = secondnumber, firstnumber
difference = firstnumber - secondnumber
print("%s m in terrain = %s mm on map" % (difference, distance))
supplement = (int((int(firstnumber) - secondnumber)*100))/100
result = (int((distance * supplement) / difference*1000))/1000
print("%s m in terrain = %s mm on map" % (supplement, result))
input("Press ENTER to continue...")