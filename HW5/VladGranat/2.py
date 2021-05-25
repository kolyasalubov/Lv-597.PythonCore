number_fibonacci = int(input("How many Fibonacci?:   "))
f1 = 0
f2 = 1
count = 0
while count < number_fibonacci:
    print(f1)
    fn = f1 + f2
    f1 = f2
    f2 = fn
    count +=1
