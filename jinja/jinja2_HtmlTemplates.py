# Import jinja2
import jinja2

# Create a new Jinja2 environment and specify the template folder
env = jinja2.Environment(loader=jinja2.FileSystemLoader('email templates'))

# Get the template file
template = env.get_template('receipt_template.html')

# Create a dictionary with the order info
order = {
    'items': [
        {'name': 'Book', 'price': 10},
        {'name': 'Pen', 'price': 1},
        {'name': 'Notebook', 'price': 5}
    ],
    'total': 16
}

# Render the template with the order info
html = template.render(order=order)

# Open a file in write mode
with open('receipt.html', 'w') as file:
    # Write the HTML string to the file
    file.write(html)