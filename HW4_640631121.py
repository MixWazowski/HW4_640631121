import itertools

n = 4
 
x = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

result = []

for permutation in itertools.permutations(str(number) for number in x):
   result.append(''.join(permutation))

maximum = max(result, key=int)

print("\nThe lragest number is:",int(maximum))