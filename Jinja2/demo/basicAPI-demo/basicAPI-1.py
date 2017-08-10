print("from jinja2 import Template")
from jinja2 import Template

print("\n")
print("template = Template(Hello {{ name }}!")
template = Template('Hello {{ name }}!')
print("template.render(name='Hongwei Hu')")
template.render(name='Hongwei Hu')
print(template.render(name='Hongwei Hu'))

print("\n")
print("t = Template(\"My favorite numbers: {% for n in range(1,10) %} {{ n }} \" \"{% endfor %}\"")
t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
print("t.render()")
t.render()
print(t.render())
