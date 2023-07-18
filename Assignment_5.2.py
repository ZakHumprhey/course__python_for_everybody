largest = None
smallest = None


while True:
    num = input("Enter a number: ")
    if num == "done":
         break
    else:
     try:
          num = int(num)
          intcheck = True
     except:
          print("Invalid input")
          continue
     if intcheck:
          if largest is None:
               largest = num
          elif num > largest:
               largest = num
          if smallest is None:
               smallest = num
          elif num < smallest:
               smallest = num
               
                
print("Maximum is", largest)
print("Minimum is", smallest)
