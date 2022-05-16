# Functions


def computepay(hrs, rate):
  if hrs>40:
    extra=hrs-40
    pay=(40+1.5*extra)*rate

  else:
    pay=hrs*rate

  return pay


hrs = float(input("Enter hours worked: "))
rate = float(input("Enter rate per hour: "))

p = computepay(hrs, rate)
print("Pay: ", p)
