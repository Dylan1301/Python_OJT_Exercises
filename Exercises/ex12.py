# Request for a specific number
# Handle failure
try:
    num = int(input("Type in the number of fibonanci number you want to get: "))
except ValueError as err:
    raise ValueError("Invalid Input - Cannot be casted into integer \n " + err.args)



numlist = [0,1]

if num < 1:
    print("Invalid position, require integer > 0")

elif num == 1:
    print(numlist[0])

elif num == 2:
    print(numlist)

else:
    for i in range(2, num):
        numlist.append( numlist[-1] + numlist[-2])
    print(numlist)


#end