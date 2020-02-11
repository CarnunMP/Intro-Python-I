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

# If sqrt(n) is a whole number, n isn't prime.
import math

if math.sqrt(n).is_integer():
    print(f"{n} is not prime.")
    exit()

# If no, do any m < sqrt(n), where m >= 2, divide into n without remainder?
m = int(math.sqrt(n))
while m > 1:
    # If yes, n isn't prime.
    if n % m == 0:
        print(f"{n} is not prime.")
        exit()

    m -= 1

# If no, n is prime.
print(f"{n} is prime!")
exit()

# So... it works! But now I'm thinking: There's no need to check even numbers.
# Or multiples of three. Or five. Etc.
# Which is exactly the idea behind The Sieve!


    