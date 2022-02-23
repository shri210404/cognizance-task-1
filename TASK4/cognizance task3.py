list = []
n = int(input("Enter number of rows : "))
print("Enter the roll number , name and marks respectively to output a data table")
for i in range(0, n):
    ele = [input(), input(),input()]
    list.append(ele)
print("Enter the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for a in list:
    for b in a:
        print(b,end=" "*10)
    print()
    
#second subdivision
list = []
n = int(input("Enter number of elements : "))
print("Enter the roll number , name and marks respectively to output a data table")
for i in range(0, n):
    ele = [input(), input(),input()]
    list.append(ele)
print("Enter the header for the created table")
print("{:<10} {:<10} {:<10} ".format(input(), input(),input()))
for i in range(3):
    print(list[1][i], end=" "*10)
