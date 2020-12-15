# Creating a GCD function
 
def gcd(num1,num2):
 
if num1==0:
		
   return num2
	
else:
		
    return(gcd(num2%num1,num1)) 


# Taking 2 numbers as input
 
a = int(input("Enter the first number : "))

b = int(input("Enter the second number : "))


# Computing the LCM and GCD

ans1 = gcd(a,b)
ans2 = a*b//ans1 

# Printing the answer

print("The GCD of 2 numbers is " + str(ans1) + " and the LCM is "+ str(ans2))
