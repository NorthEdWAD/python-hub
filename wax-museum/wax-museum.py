def calculate_sum(num1, num2): 
    grand_total = num1 + num2
    return f"{num1} plus {num2} equals {grand_total}."

first_num = 10
second_num = 3
# Call the function, then display the answer
print(calculate_sum(first_num, second_num))


def welcome_user(first_name, last_name):
    return f"Welcome, {first_name.title()} {last_name.title()}!"

my_first_name = "abraham"
my_last_name = "lincoln"
print(welcome_user(my_first_name, my_last_name))