inputString = "Testing"

def StringHash(word, primeNumber = 31):
    hashVal = 0
    size = len(word)
    for i in range(size):
        hashVal += ord(word[i])*primeNumber**(size - i)

    return hashVal

print(StringHash(inputString))
