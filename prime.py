def is_prime(n):

    for i in range(2,n):
        if n%i == 0:
            print "The number entered is not prime"
            return False
        else :
            print "The number entered is prime"
            return True