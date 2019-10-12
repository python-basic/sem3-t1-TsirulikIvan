import math

def geron():
    a = input('Enter size of first side:\n')
    b = input('Enter size of second side:\n')
    c = input('Enter size of third side:\n')
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))



if __name__ == "__main__":
    print(geron())
    
