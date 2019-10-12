def sum():
    first_num = input('Enter the first number of progression:\n')
    inc = input('Enter the increment number:\n')
    n = input('ENter the N:\n')
    sum = first_num
    for i in range(n - 1):
        first_num += inc
        sum += first_num
    return sum
    
if __name__ == "__main__":
    print(sum())
