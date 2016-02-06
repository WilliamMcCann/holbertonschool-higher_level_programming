#shebang advising python where python can be found

#!/usr/bin/python

#required comment introducing myself and the purpose of the program

"""Hello! I'm William McCann, Software Engineer at the Holberton School.  This is a Python program I've written to let you calculate the total bill of a meal by calculating the taxes and tip and adding it all together for you.  Enjoy!  You can reach out to me with feedback at @NWMcCann"""

#prints the welcome text

print "Welcome to the taxes and tip calculator!"

"""gets input on the meal price and assigns it to variable "meal".  Converts that to an int so it can be used for math"""
meal = float(raw_input("What is the price before tax? "))

"""gets input on the tax amount and assigns it to variable "taxes" Converts that to an int so it can be used for math"""
taxes = float(raw_input("What are the taxes? (in %) "))

"""gets input on the tip amount and assigns it to variable "tip" Converts th\
at to an int so it can be used for math"""
tip = float(raw_input("What do you want to tip? (in %) "))

"""divides variable "taxes" by 100 to convert it to a percentage.  Multiplies that by "meal" to get the amount of the tip.  Adds that to meal to get the amount of the meal and taxes combined.  Assigns that to variable "meal_and_taxes" """
meal_and_taxes = meal + (meal * (taxes / 100))

"""divides variable "tip" by 100 to convert it to a percentage.  Multiplies that times variable "meal_and_taxes" and then adds that to variable "meal_and_taxes" to get the total amount of the meal and taxes and tip.  Assigns that to variable "total"  """
total = meal_and_taxes + (meal_and_taxes * (tip / 100))

"""Prints the result in a sentence with the variable "total" as a floating point number with six digits after the decimal point"""
print "The price you need to pay is: $%.6f." % (total)

