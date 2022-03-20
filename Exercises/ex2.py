from math import sqrt

while True:
    try:
        num = int(input("Enter an integer number: "))

        break
    except ValueError:
        print("Your input value is not valid, please retry")



# Function to test whether a given number is a prime number
def isPrimeNumber(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
        else:
            continue
    return True

primeList = []


for i in range(num):
    if isPrimeNumber(i):
        primeList.append(i)
    else:
        continue

print("All prime number that are smaller than the input integer are:")
print(primeList)
