fname = input("Enter file name: ")
fh = open(fname)
ln_count = 0
avg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ln_count += 1
    numLoc = line.find('.') - 1
    num = float(line[numLoc:])
    avg = avg + num
avg = avg / ln_count
print("Average spam confidence:", avg)
