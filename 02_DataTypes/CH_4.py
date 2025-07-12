# Boolean data type demonstration

# Assigning the boolean value True to the variable 'islogged_in'.
# This variable can be used to check if a user is currently logged in.
islogged_in = True

# Assigning the boolean value False to the variable 'is_admin'.
# This variable can be used to check if the logged-in user has administrative privileges.
is_admin = False

add_sugar = True  # Assigning True to indicate that sugar is added to the tea
how_much_sugar = 2  # Assigning the amount of sugar added, in teaspoons
total_sugar = add_sugar + how_much_sugar  # Adding the boolean and integer values; True is treated as 1
print("Total sugar added:", total_sugar)  # Displays the total amount of sugar added if 'add_sugar' is True