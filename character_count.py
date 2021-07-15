def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1 #count = count + 1
    return count
filename = input("Write text name: ")
with open(filename) as f:
    text = f.read()
print(count_char(text,'d')) #write any character what you need to count in ' '
