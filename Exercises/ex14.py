
testList = [1,2, "sdfa"]

def getAddresses(inputList: list):
    if not isinstance(inputList, list):
        raise TypeError("wrong input parameter's type - require a list")

    placesList = list(filter(lambda x: isinstance(x, str), inputList))

    return placesList

print("Address Filter Function")
print(getAddresses(testList))

# Function to test the functions
LocationList = []
while True:
    place = input("Enter text (or Enter to quit): ")
    if not place:
        break

    LocationList.append(place)

print(LocationList)
