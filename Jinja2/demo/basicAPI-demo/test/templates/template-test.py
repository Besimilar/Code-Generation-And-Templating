from jinja2 import Environment, PackageLoader
env = Environment(
    loader=PackageLoader('test', 'templates'),
    # autoescape=select_autoescape(['html', 'xml'])
    autoescape={{ escape }}
)

template = env.get_template('cloud.html')
print(template.render(latitude='42', longitude='-71'))
