from functions import highest_profit_branch, profit_of_branch, lowest_profit_branch, avg_customer_rating
from functions import popular_payment_method, read_data, most_profitable_line
import csv

# csv header
fieldnames = ['Branch', 'Most popular payment method', 'Average customer rating (%)', 'Total profit (£)',
              'Most profitable product line']

# csv data
all_data = read_data()
branches = ['A', 'B', 'C']
rows = []
i = 0
while i < len(branches):
    row = {'Branch':  branches[i],
           'Most popular payment method': popular_payment_method(branches[i]),
           'Average customer rating (%)': avg_customer_rating(branches[i]),
           'Total profit (£)': profit_of_branch(branches[i]),
           'Most profitable product line': most_profitable_line(branches[i])}
    rows.append(row)
    i += 1


with open('supermarket_sales_branch_analysis.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# With more time I would have calculated most profitable time of day and day of the week