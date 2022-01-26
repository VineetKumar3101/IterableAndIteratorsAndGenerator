print("\n----------------------------------------------------")

print("ITERABLE")

str="VineetKumar"
for i in str:
    print(i)

print("\n-----------------------------------------------------")


list=[3,4,5,6,8,9]
for j in list:
    print(j)

print("\n-----------------------------------------------------")



print("\n-----------------------------------------------------")


print("ITERATORS")

Marks=[45,67,88,66,22,88,100]
it1=iter(Marks)
print(next(it1))
print(next(it1))

print("\n-----------------------------------------------------")

print("GENERATOR")

#odd number program by generator
def My(n):
    for i in range(1,n+1,2):
        yield i
it1=My(1000)
print(it1)
print(next(it1))
print(next(it1))


print("\n-----------------------------------------------------")

#loop for the above program

for i in range(1,100,2):
    print(i)
print("\n-----------------------------------------------------")

#creating second generator

it2=My(2000)
print(it2)
print(next(it2))
print("\n-----------------------------------------------------")