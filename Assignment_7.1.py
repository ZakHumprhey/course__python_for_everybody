fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read().upper().rstrip()

print(inp)
