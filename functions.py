import csv
from collections import Counter


# Reads data into a list of dictionaries
def read_data():
    data = []
    with open('supermarket_sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(dict(row))

    return data


# Returns the profit of a branch
def profit_of_branch(branch):
    all_data = read_data()
    i = 0
    profits_branch = []
    while i < len(all_data):
        if all_data[i]['Branch'] == branch:
            profit_branch = float(all_data[i]['Unit price']) * float(all_data[i]['Quantity'])
            profits_branch.append(profit_branch)
        i += 1

    total_profit_branch = round(sum(profits_branch))
    return total_profit_branch


# Returns the branch with the highest profits
def highest_profit_branch():
    branch_profits_dict = {'A': profit_of_branch('A'), 'B': profit_of_branch('B'), 'C': profit_of_branch('C')}
    highest_value = max(branch_profits_dict, key=branch_profits_dict.get)
    return highest_value, branch_profits_dict[highest_value]


# Returns the branch with the lowest profits
def lowest_profit_branch():
    branch_profits_dict = {'A': profit_of_branch('A'), 'B': profit_of_branch('B'), 'C': profit_of_branch('C')}
    lowest_value = min(branch_profits_dict, key=branch_profits_dict.get)
    return branch_profits_dict[lowest_value]


# Returns the average customer rating of a branch
def avg_customer_rating(branch):
    all_data = read_data()
    branch_ratings = []
    i = 0
    while i < len(all_data):
        if all_data[i]['Branch'] == branch:
            rating = float(all_data[i]['Rating'])
            branch_ratings.append(rating)
        i += 1

    avg_rating = sum(branch_ratings)/len(branch_ratings)
    return round(avg_rating, 2)


# Returns the most popular payment method of a branch
def popular_payment_method(branch):
    all_data = read_data()
    payment_methods = []
    i = 0
    while i < len(all_data):
        if all_data[i]['Branch'] == branch:
            payment_method = all_data[i]['Payment']
            payment_methods.append(payment_method)
        i += 1

    payment_methods_results = Counter(payment_methods)
    most_popular_payment = max(payment_methods_results)

    return most_popular_payment


# Returns most profitable product line of a branch
def most_profitable_line(branch):
    all_data = read_data()
    product_lines = ['Electronic accessories', 'Fashion accessories', 'Food and beverages', 'Health and beauty',
                     'Home and lifestyle', 'Sports and travel']

    electronics_profits = 0
    fashion_profits = 0
    food_profits = 0
    health_profits = 0
    home_profits = 0
    sports_profits = 0
    i = 0
    while i < len(all_data):
        if (all_data[i]['Branch'] == branch) & (all_data[i]['Product line'] == 'Electronic accessories'):
            profit = int(float(all_data[i]['Unit price']) * float(all_data[i]['Quantity']))
            electronics_profits += profit
        elif (all_data[i]['Branch'] == branch) & (all_data[i]['Product line'] == 'Fashion accessories'):
            profit = int(float(all_data[i]['Unit price']) * float(all_data[i]['Quantity']))
            fashion_profits += profit
        elif (all_data[i]['Branch'] == branch) & (all_data[i]['Product line'] == 'Food and beverages'):
            profit = int(float(all_data[i]['Unit price']) * float(all_data[i]['Quantity']))
            food_profits += profit
        elif (all_data[i]['Branch'] == branch) & (all_data[i]['Product line'] == 'Health and beauty'):
            profit = int(float(all_data[i]['Unit price']) * float(all_data[i]['Quantity']))
            health_profits += profit
        elif (all_data[i]['Branch'] == branch) & (all_data[i]['Product line'] == 'Home and lifestyle'):
            profit = int(float(all_data[i]['Unit price']) * float(all_data[i]['Quantity']))
            home_profits += profit
        elif (all_data[i]['Branch'] == branch) & (all_data[i]['Product line'] == 'Sports and travel'):
            profit = int(float(all_data[i]['Unit price']) * float(all_data[i]['Quantity']))
            sports_profits += profit

        i += 1

    product_lines_profits = {product_lines[0]: electronics_profits,
                             product_lines[1]: fashion_profits,
                             product_lines[2]: food_profits,
                             product_lines[3]: health_profits,
                             product_lines[4]: home_profits,
                             product_lines[5]: sports_profits,
                             }

    most_profitable = max(product_lines_profits, key=product_lines_profits.get)
    return most_profitable
