
#our boss wants us to convert a bunch of temperatures from celsius to farenheit
print ((20 * 9/5) + 32)
print ((50 * 9/5) + 32)
print ((32 * 9/5) + 32)
print ((12 * 9/5) - 32)  #we typed tye formula wrong here!
print ((39 * 9/5) + 32)
print ((21 * 9/5) + 32)  #we made a data entry error!

#we have a tool for this!  we'll use a collection (a list in this case) and a trusty loop
temperature_list = [20, 50, 32, 12, 50, 39, 20] 

for x in temperature_list:
    print ((temperature * 9/5) + 32)


#moving to a function - code is in one place, and it reads much nicer
def temperature_conversion(inTemp):
    return (temperature * 9/5) + 32

for temperature in temperature_list:
    print (temperature_conversion(temperature) )

#he called up on friday afternoon and he's mad at you! you figure out he meant that these WERE farenheit and wants to go TO celsius

def temperature_conversion(inTemp):
    return (temperature  - 32) * 5/9

for temperature in temperature_list:
    print (temperature_conversion(temperature) )

# now he wants us to print it nicely!  This guy, really...
def printNiceForBoss(inNumberToPrint):
    formatted_number = "{:.1f}".format(inNumberToPrint)
    print(formatted_number)

for temperature in temperature_list:
    printNiceForBoss (temperature_conversion(temperature) )


#what would this have looked like?
print(f"{((21 * 9/5) + 32):.1f}")
print(f"{((50 * 9/5) + 32):.1f}")
print(f"{((23 * 9/5) + 32):.1f}")
print(f"{((36 * 9/5) + 32):.1f}")
print(f"{((11 * 9/5) + 32):.1f}")
print(f"{((11 * 9/5) + 32):.1f}")

