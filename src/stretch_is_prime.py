# Okay. First thought is: Is sqrt(n) a whole number? If yes, n isn't prime.
# If no, do any m < sqrt(n), where m >= 2, divide into n without remainder?
# If yes, n isn't prime.
# If no, n is prime.

# This should be a simple enough alg... but it's nowhere near as efficient
# as The Sieve of Eratosthenes!

# Oh well. I'll give both a shot. :)

# Some things to consider before charging ahead:
# - Want program to take a single argument, n
# - Want n to be an integer
# - Want n to be greater than 1
# - Want to ignore leading 0s

import sys

n = 0
if len(sys.argv) != 2:
    print("Error: Please provide a single, integer argument greater than 1.")
    exit()
elif "." in sys.argv[1]:
    print("Error: You provided a float. Please provide an integer greater than 1.")
    exit()
else:
    try:
        n += int(sys.argv[1])
        if n <= 0:
            print("Error: Please provide an integer greater than 1.")
            exit()
        elif n == 1:
            print("1 is not prime. Please provide an integer greater than 1.")
            exit()
    except ValueError:
        print("Error: You provided a string, or something else. Please provide an integer greater than 1.")
        exit()
    except SyntaxError:
        inputStr = sys.argv[1]

        while "0" in inputStr:
            inputStr = inputStr[1:]

        n = int(sys.argv[1])

# Okay. With the input now tidied up...

import math

# If sqrt(n) is a whole number, n isn't prime.
if math.sqrt(n).is_integer():
    print(f"Carnun's hacky algorithm says: {n} is not prime.")
    # exit()

# If no, do any m < sqrt(n), where m >= 2, divide into n without remainder?
else:
    m = int(math.sqrt(n))
    divisorFound = False
    while m > 1:
        if n % m == 0:
            divisorFound = True
            break
        m -= 1
    
    if divisorFound:
        # If yes, n isn't prime.
        print(f"Carnun's hacky algorithm says: {n} is not prime.")
    else:
        # If no, n is prime.
        print(f"Carnun's hacky algorithm says: {n} is prime!")

# So... it works! But now I'm thinking: There's no need to check even numbers.
# Or multiples of three. Or five. Etc.
# Which is exactly the idea behind The Sieve!

# Need an array of bools, to keep track of whether an integer m, where 1 < m < sqrt(n), has been visited.
visited = [False for i in range(int(math.sqrt(n)))]
toCheck = [i + 2 for i in range(int(math.sqrt(n)))]

### Helper
def checkNotPrime(n, m):
    if n == 2:
        print(f"The Sieve of Erastosthenes says: {n} is prime!")
        exit()
    if n % m == 0:
        print(f"The Sieve of Erastosthenes says: {n} is not prime.")
        exit()
###

for m in toCheck:
    if not visited[m - 2]:
        visited[m - 2] = True

        checkNotPrime(n, m)

        j = 0
        while m**2 + m*j < math.sqrt(n):
            visited[(m**2 + m*j) - 2] = True

            checkNotPrime(n, m)

            j += 1

print(f"The Sieve of Erastosthenes says: {n} is prime!")
exit()