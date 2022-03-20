
print("Question 3a")

inputString  = input("Type in a string for reverse string: ")
print(inputString[::-1])


print("\n Question 3b")
input3b  = input("Type in a sentence for reverse words: ")
print(" ".join(input3b.split()[::-1]))