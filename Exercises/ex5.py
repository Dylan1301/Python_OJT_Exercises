import random
import string


specialChar = list((random.choice('!@#$%^&*') for i in range(2)))
digits = list(random.choice(string.digits) for i in range(2))
upperChar = list(random.choice(string.ascii_uppercase) for i in range(3))
lowerChar = list(random.choice(string.ascii_lowercase) for i in range(3))


CharChoice = specialChar + digits + upperChar + lowerChar

random.SystemRandom().shuffle(CharChoice)
password = ''.join(CharChoice)

print(password)