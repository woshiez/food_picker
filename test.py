
import random

Places = []

while True:
  	newplace = input("add new choices? (enter 'no' to stop): ")
  	if (newplace != "no"):	
  	    Places.append(newplace)
  	else:
  	    break

if not Places:
    print("can't pick if you don't enter any choices")
else:
    choice = Places[random.randint(0,len(Places)-1)]
    print(f"The food AI insists that you eat: {choice}")
