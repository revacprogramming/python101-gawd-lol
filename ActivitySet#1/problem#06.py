# Loops & Iterators

largest = None
smallest = None

while True:
  try:
      num = input("Enter a number: ")

      if num == "done":
          break

      inum=int(num)
      if largest==None or inum>largest:
        largest=inum
      elif smallest==None or inum<smallest:
        smallest=inum

  except:
      print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
