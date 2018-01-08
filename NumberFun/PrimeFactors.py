#find the prime factors of a given number

#going to use the sieve to find primes up to the input//2
def generate(limit):
    primes = [2]
    if limit <=1 :
        primes = []
    elif limit == 2: pass
    else:
        #stepsize is two, as no evens are prime other than 2
        for i in range(3,limit+1,2):
            for j in range(0,len(primes)):
                if i%primes[j] == 0:
                    break
                elif len(primes) == j+1:
                    primes.append(i)
    return primes

def factor(number):
    primez = generate(number//2)
    factors = []
    for i in primez:
        if number == 1 or number ==0:break
        while number % i == 0:
            number = number / i
            factors.append(i)
    return factors


def main():
    userinput = ""
    while userinput !="exit":
        userinput = input("Get dem prime factors: \n")
        print(factor(int(userinput)))

if __name__ == "__main__":
    main()
