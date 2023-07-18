def computepay(h, r):
    h = float(h)
    r = float(r)
    if h >= 40.0:
         ot = h - 40.0
         return (40 * r  + (ot * (r * 1.5)))
    else:
         return (h*r)
            
            
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs, rate)
print("Pay", p)
