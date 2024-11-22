# giving instructions oh how to order
print("Enter 'quit' to finish your order.")
print("Maximum number of toppings is 10.")

# using for loop for entering multiple toppings
for i in range(10):
    topping = input("Enter your toppings: ")
    
    if topping.lower() == "quit":
        print("Your order is complete.")
        break
    else:
        print(f"I'll add {topping} to your pizza.")
        

