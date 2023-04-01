N=int(input("Enter the value of N: "))
for N in range(1,16):
    if N % 3 == 0 and N % 5 == 0:
        print("fizzbuzz")
        continue
    elif N % 3 == 0:
        print("fizz")
        continue
    elif N % 5 == 0:
        print("buzz")
        continue
    print(N)