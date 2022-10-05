# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("Please enter an amount less than a dollar.")
change=100-int(input())
quarters=change//25
dimes=(change%25)//10
nickels=((change%25)%10)//5
pennies=(((change%25)%10)%5)
print("Your change will be:")
print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)


