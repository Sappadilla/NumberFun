#use the sieve to determine and display all prime numbers below 10 milly

class sieve(object):

    def __init__(self):
        self.primes = [2]

    #output is a list of primez
    def generate(self,limit):
        self.primes = [2]
        if limit <=1 :
            self.primes = []
        elif limit == 2: pass
        else:
            #stepsize is two, as no evens are prime other than 2
            #lol right here I even almost did it right by accident
            for i in range(3,limit+1,2):
                for j in range(0,len(self.primes)):
                    if i%self.primes[j] == 0:
                        break
                    elif len(self.primes) == j+1:
                        self.primes.append(i)

    def actualSieve(self,limit):
        self.primes = [2]
        self.numz = []
        if limit <=1 : self.primes = []
        elif limit == 2: pass
        else:
            for i in range(2,limit+1):
                for j in range(1,limit//i):
                    #check if i is in list
                    #if it isnt, add and add to prime list
                    #then add it's multiples up to the limit
                    if self.numz

def main():
    primers = sieve()
    primers.generate(100000)
    print(primers.primes)

if __name__ =="__main__":
    main()