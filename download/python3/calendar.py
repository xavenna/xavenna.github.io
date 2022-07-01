#A random calendar fact generator based on xkcd.com/1930
#By xavenna
#Note: remake for xkcd #2243
import random
#Lists of content
a1 = "Did you know that"
a2 = ["The %1% Equinox", "The %2% %3%", "The %4% %5%", "Daylight %6% Time", "Leap %7%", "Easter", "The %8% Moon", "Toyota Truck Month", "Shark Week"]
b2 = [["Fall", "Spring"], ["Winter", "Summer"], ["Solstice", "Olympics"], ["Earliest", "Latest"], ["Sunrise", "Sunset"], ["Saving", "Savings"], ["Day", "Year"], ["Harvest", "Super", "Blood"]]
a3 = ["Happens %1% Every Year", "Drifts out of sync with the %2%", "Might %3% This Year"]
b3 = [["Earlier", "Later", "At the wrong time"], ["Sun", "Moon", "Zodiac", "Gregorian Calendar", "Mayan Calendar", "Lunar Calendar", "iPhone Calendar", "Atomic Clock in Colorado"], ["Not happen", "Happen twice"]]
a4 = "because of"
a5 = ["Time Zone Legislation in %1%", "A Decree by the Pope in the 1500s", "%2% of the %3%", "Magnetic field reversal", "An arbitrary decision by %4%"]
b5 = [["Indiana", "Arizona", "Russia"], ["Precession", "Libration", "Nutation", "Libation", "Eccentricity", "Obliquity"], ["Moon", "Sun", "Earth's axis", "Equator", "Prime meridian", "International date line", "Mason Dixon line"], ["Benjamin Franklin", "Isaac Newton", "FDR"]]
a6 = "? Apparently"
a7 = ["It causes a predictable increase in car accidents.", "That's why we have leap seconds.", "Scientists are really worried.", "It was even more extreme during the %1%.", "There's a proposal to fix it, but it %2%", "It's getting worse and no one knows why."]
b7 = [["Bronze age", "Ice age", "Cretaceous", "1990s"], ["Will never happen", "Actually makes things worse", "Is stalled in Congress", "might be unconstitutional"]]
a8 = "While it may seem like trivia, it"
a9 = ["causes huge headaches for software developers", "is taken advantage of by high-speed traders", "triggered the 2003 Northeast Blackout", "Has to be correced for by GPS satelites", "Is now recognized as a major cause of World War I"]
#Fact generator
temp = a1 + " " + a2[random.randint(0,8)]
for x in range(len(temp)):
  if temp[x] == "%":
    temp2 = int(temp[x+1:x+2])-1
    temp = temp[0:x] + b2[temp2][random.randint(0,len(b2[temp2])-1)] + temp[x+3:]
    break
for x in range(len(temp)): 
  if temp[x] == "%":
    temp2 = int(temp[x+1:x+2])-1
    temp = temp[0:x] + b2[temp2][random.randint(0,len(b2[temp2])-1)] + temp[x+3:]
    break
temp += " " + a3[random.randint(0,2)]
for x in range(len(temp)): 
  if temp[x] == "%":
    temp2 = int(temp[x+1:x+2])-1
    temp = temp[0:x] + b3[temp2][random.randint(0,len(b3[temp2])-1)] + temp[x+3:]
    break
temp += " " + a4 + " " + a5[random.randint(0,4)]
for x in range(len(temp)): 
  if temp[x] == "%":
    temp2 = int(temp[x+1:x+2])-1
    temp = temp[0:x] + b5[temp2][random.randint(0,len(b5[temp2])-1)] + temp[x+3:]
    break
for x in range(len(temp)): 
  if temp[x] == "%":
    temp2 = int(temp[x+1:x+2])-1
    temp = temp[0:x] + b5[temp2][random.randint(0,len(b5[temp2])-1)] + temp[x+3:]
    break
temp += a6 + " " + a7[random.randint(0,5)]
for x in range(len(temp)): 
  if temp[x] == "%":
    temp2 = int(temp[x+1:x+2])-1
    temp = temp[0:x] + b7[temp2][random.randint(0,len(b7[temp2])-1)] + temp[x+3:]
    break
temp += " " + a8 + " " + a9[random.randint(0,4)]
print(temp)
