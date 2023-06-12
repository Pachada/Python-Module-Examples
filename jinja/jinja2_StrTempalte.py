from jinja2 import Template

template = Template("Hello {{ name }}!")
html_str = template.render(name="John")
print(html_str) # Hello John!