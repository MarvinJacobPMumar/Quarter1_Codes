
# Function
def calculate (d, r): 
  fee = d * r
  fee = round(fee, 2)
  return fee

# Inputs
distance = float(input("Enter distance in kilometers: "))
rate = float(input("Enter rate per kilometer (#): "))

# Output
print("Total Delivery Fee: " + str(calculate(distance, rate)))
