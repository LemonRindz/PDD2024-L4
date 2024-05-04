#Imani Hollie 02.02.2024
#This program takes the total seats sold per class and calculates
#the total seats sold and the total sales made.

#Declare the main module [Inputs and Calls totalSales()]
#1. main()
    #Declare local variables
    #a. Declare Float aSeat
    #b. Declare Float bSeat
    #c. Declare Float cSeat
    
    #Input for total seats sold per class
    #d. Display "Enter total class A seat tickets sold: "
    #e. Input aSeat
    #f. Display "Enter total class B seat tickets sold: "
    #g. Input bSeat
    #h. Display "Enter total class C seat tickets sold: "
    #i. Input cSeat

    #Call the totalSales module and passes aSeat, bSeat,
    #and cSeat as reference
    #j. Call totalSales(aSeat, bSeat, cSeat)
#1. End Module

#Output is then printed to the screen.

#Declare the totalSales module [Calculates and Outputs]
#2. Module totalSales(Float Ref classA, Float Ref classB, Float Ref classC)
    #Declare variables
    #a. Declare Float totalSeats
    #b. Declare Float aSale
    #c. Declare Float bSale
    #d. Declare Float cSale
    #e. Declare Float totalSales

    #Calculate the total seats sold, total sals made per class sold, and total sales made
    #f. Set totalSeats = classA + classB + classC
    #g. Set aSale = classA * 15
    #h. Set bSale = classB * 12
    #i. Set cSale = classC * 9
    #j. Set totalSales = aSale + bSale + cSale

    #Display total seats sold per class, total seats sold,
    #total sales made per class, and total sales made
    #k. Display "Total Class A Seats: ", classA
    #l. Display "Total Class B Seats: ", classB
    #m. Display "Total Class C Seats: ", classC
    #n. Display "Total Seats Sold: ", totalSeats
    #o. Display "Total Class A Sales: ", aSale
    #p. Display "Total Class B Sales: ", bSale
    #q. Display "Total Class C Sales: ", cSale
    #r. Display "Total Sales Made: ", totalSales
#2. End Module