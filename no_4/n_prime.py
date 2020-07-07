"""
Find first N prime number, and print the result
Input: 4
Output : 2, 3, 5, 7

"""


class PrimeBuilder(object):
    def is_prime(self, x):
        # if there is any number between 1 and x-1 that can divide x, then x is not prime
        return not any(x // i == x / i for i in range(x - 1, 1, -1))

    def n_prime(self, n):
        prime_arrays = []
        x = 2
        while len(prime_arrays) < n:
            if self.is_prime(x):
                prime_arrays.append(x)
            x += 1
        return prime_arrays


if __name__ == "__main__":
    pb = PrimeBuilder()
    n = None
    while n is None:
        try:
            n = int(input("How many prime numbers do you want to find?: "))
        except ValueError:
            print("Not an integer value...")
    prime_arrays = pb.n_prime(n)

    # The value will be printed and saved as array like [2, 3, 5, 7] not string like "2, 3, 5, 7" to make the unittest easier.
    print(prime_arrays)

