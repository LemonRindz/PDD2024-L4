#Imani Hollie 02.02.2024
#This program takes the total replacement cost for property and
#calculates the minimum amount of insurance recommended to cover it.

#Declare the main module [main() input and calls minIns()]
#1. main() 
    #Declare local variables
    #a. Declare Float totalCost

    #Input total for property
    #b. Display "Enter the total replacement cost for property: "
    #c. Input totalCost

    #Call the minIns module and pass totalCost as reference
    #d. Call minIns(totalCost)
#1. End Module
#Output is then printed to the screen.

#Declare the minIns module [minIns() calculates and outputs]
#2. Module minIns(Float Ref minInsCov)
    #Declare variables
    #a. Declare Float minInsCov
    
    #Calculate the minimum recommended insurance coverage
    #b. Set minInsCov = totalCost * 0.8

    #Display total replacement cost and minimum recommended insurance coverage
    #c. Display "Total Replacement Cost: ", totalCost
    #d. Display "Minimum Insurance Cost: ", minInsCov
#2. End Module