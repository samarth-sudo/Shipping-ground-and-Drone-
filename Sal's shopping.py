#In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

#Sal’s Shippers has several different options for a customer to ship their package:

#Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
#Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
#Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
#VARIABLE DECLARATION
weight = float(input("Enter the amount of weight: "))
#GROUND SHIPPING
if weight <= 2:
  cost_ground = weight *1.5 +20
elif  weight <=6:
 cost_ground = weight*3.00 + 20
elif weight <=10:
 cost_ground = weight*4.00 + 20
else:
  cost_ground = weight*4.75 + 20
cost_premium_ground=125.00
print("Cost of premium ground shipping $",cost_premium_ground)

print("Cost of ground shipping $: ",cost_ground)

#DRONE SHIPPING
weight= float(input("Enter the wieght for the drone shipping:  "))
if weight <= 2:
  cost_drone =weight * 4.50 + 0.00
elif weight <= 6:
  cost_drone = weight * 9.00 + 0.00
elif weight <=10 :
  cost_drone = wieght * 12.00 + 0.00
else:
  cost_drone =weight * 14.25 + 0.00

print("Cost of using the drone shipping$", cost_drone)


