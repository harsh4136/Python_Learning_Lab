n = int(input("Enter the size of loop : "))

def perfect_Number(n) :
    if n < 1:
        return False
    
    perfect_sum = 0
    for i in range(1,n):
        if n%i==0:
            perfect_sum += i
    return perfect_sum == n

for i in range(1,n+1):
    if perfect_Number(i):
        print(i,end=",")
        


    
        
  