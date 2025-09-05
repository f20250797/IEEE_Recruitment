para = input("Enter paragraph: ")
words = para.split()
count = 0
for i in words:
    rev = i[::-1]
    if i==rev:
        count+=1
        print(i)
print(count)
