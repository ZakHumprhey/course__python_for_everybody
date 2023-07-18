text = "X-DSPAM-Confidence:    0.8475"

periodLoc = text.find('.')

print(float(text[(periodLoc - 1):]))
