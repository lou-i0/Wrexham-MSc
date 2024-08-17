def multiply(x,y):
    answer = 0
    while y > 0:
        answer += x
        y  -= 1  
    return answer
    
    
print(multiply(5,7))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(6))


def movetower(height,fromPole, toPole, withPole):
    if height >=1:
        movetower(height -1, fromPole, withPole, toPole)
        movedisk(fromPole, toPole)
        movetower(height-1,withPole,toPole,fromPole)
        
def movedisk(fp,tp):
    print(f'moving disk from {fp}, to {tp}')
    
movetower(3,'A','B','C')