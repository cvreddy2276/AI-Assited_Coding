import math

class Task2:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            print(f"{n} is not a prime number.")
            return
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                print(f"{n} is not a prime number.")
                return
        print(f"{n} is a prime number.")

if __name__ == "__main__":
    Task2.is_prime(17)
    Task2.is_prime(20)