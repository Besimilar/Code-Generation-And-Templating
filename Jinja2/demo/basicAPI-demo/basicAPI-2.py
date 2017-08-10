from jinja2 import Environment, PackageLoader
env = Environment(
    loader=PackageLoader('test', 'templates'),
    # autoescape=select_autoescape(['html', 'xml'])
    autoescape=True
)

print("########### 1st Test ###########")
template = env.get_template('cloud.html')
print(template.render(latitude='42', longitude='-71'))

print("\n")
print("########### 2nd Test ###########")
template = env.get_template('template-test.py')
print(template.render(escape='TRUE'))
