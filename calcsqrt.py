#! /usr/bin/env python3

# Nathan Garrihy
# Calculate square root of a number.

def sqrt(x):
  """
  Calculate the square root of argument x.
  """
  # Check that x is positive
  if (x < 0):
      print("Error: negativev value supplied")
      return -1
  else:
      print("Here we go")

  # Initial guess for the square root
  z = x / 2.0

  # Continiously improve the guess 
  # Adaprted from http://tour.golang.org/flowcontrol/8
  while abs(x - (z*z)) > 0.01:    # abs returns absolute value (always positive value of number)
    z = z - (((z*z) - x) / (2*z))

  return z

myval = 63.0
print("The square root of", myval, "is: ",  sqrt(myval))


