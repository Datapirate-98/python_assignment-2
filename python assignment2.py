1.
for i in range(5):
    for j in range(0,i+1):
        print("*", end = "")
    print("\r")

for i in range(4,0,-1):
    for j in range(0,i):
        print("*", end = "")
    print("\r")

2. 
word = input("Input word: ")
print("Output: "word[::-1])
