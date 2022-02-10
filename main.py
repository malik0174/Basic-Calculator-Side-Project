# This program will function as a basic calculator that will
# add, subtract, multiply, and divide any two numbers

# This function will add two numbers
def addFunction(num1, num2):
  return num1 + num2

# This function will subtract two numbers
def minusFunction(num1, num2):
  return num1 - num2

# This function will multiply any two numbers
def multiplyFunction(num1, num2):
  return num1 * num2

# This function will divide any two numbers
def divideFunction(num1, num2):
  return num1 / num2

# Asking the user for which operation they would like performed
print("What operation would you like to perform...")
print()
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")
print()

while True:
  # Taking user input
  user_choice = input("Indicate the operation of your choosing by selecting its corresponding integer: \n")

  # checking if choice is one of the 4 options
  if user_choice in ('1', '2', '3', '4'):
    user_num1 = float(input("Enter your first number: "))
    user_num2 = float(input("Enter your second number: "))

    if user_choice == '1':
      print(user_num1, "+", user_num2, "=", addFunction(user_num1, user_num2))                                                   
    elif user_choice == '2':
      print(user_num1, "-", user_num2, "=", minusFunction(user_num1, user_num2))

    elif user_choice == '3':
      print(user_num1, "*", user_num2, "=", multiplyFunction(user_num1, user_num2))
            
    elif user_choice == '4':
      print(user_num1, "/", user_num2, "=", divideFunction(user_num1, user_num2))

    else:
      print("Please restart the program and input a valid answer")

    # Checking if the user wants to perform another calculation. If the answer is no
    # then the while loop will break
    future_calculation = input("Would you like to perform another calculation? (yes/no): ")
    if future_calculation == "no":
      break

    elif future_calculation == "yes":
      continue
    
    else:
      print("Please type in a valid answer")