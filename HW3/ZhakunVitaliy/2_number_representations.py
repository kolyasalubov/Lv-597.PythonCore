x = input("Enter any 4-digit natural number: \n")
print(f"You have just entered the number: {x}")

res = "RESULTS".center(50, "=")
print(res)
nlist = list(x)
mult = eval('*'.join(nlist))
print(f"The multiplication of all digits is: {str(mult).rjust(12,'.')}")

print('-'*50)

reverse = "".join(nlist[::-1])
print(f"The reversed representation of the number: {reverse.rjust(6,'.')}")

print('-'*50)


nlist.sort()
n_sort = "".join(nlist)
print(f"The sorted representation of the number: {n_sort.rjust(8,'.')}")
