def analyze_number():

    check = True
    z = 0
    while check == True:
        
        n=input ("Enter an integer between 1 and 1000000:  ")
        
        if n in range(1,1000001):
            
            if n%2 == 0:
                print "The number entered is even"
            else :
                print "The number entered is not even"
                    
            for i in range(2,n-1):
                if n%i == 0:
                    z=1 
            if z==1 :  
                print "The number entered is not prime" 
            else :   
                print "The number entered is prime"
                
            check = input ("Enter True to continue or False to quit   ")
            z=0
        else:
            print "Number is not an integer or not in span"
            check = False
            return False