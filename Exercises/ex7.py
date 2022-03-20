numbers = [x for x in range(101)]

odd = [x for x in numbers if x %2 == 1]
even = [x for x in numbers if x %2 == 0]

oddfilter = list(filter(lambda x: x%2==1, numbers))
evenfilter = list(filter(lambda x: x%2==0, numbers))

print("The odd number list: {}".format(odd))
print("The even number list: {}".format(even))


