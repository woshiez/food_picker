
import random

Places = []
morestuff = True

while 	morestuff == True:
  	newplace = raw_input("add new choices? 'no' to stop: ")
    	if (newplace != "no"):	
      		Places.append(newplace)
    	else:
      		morestuff = False

print(Places[random.randint(0,len(Places)-1)])
print(len(Places)-1)



