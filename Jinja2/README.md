# Jinja (Jinja2)
Jinja, also known and referred to as "Jinja2", is a popular Python template engine written as a self-contained open source project.

Jinja2 is one of the most used template engines for Python. It is inspired by Django's templating system but extends it with an expressive language that gives template authors a more powerful set of tools.

## Features:
1. powerful automatic HTML escaping system for cross site scripting prevention.
2. Template inheritance makes it possible to use the same or a similar layout for all templates.
3. High performance with just in time compilation to Python bytecode. Jinja2 will translate your template sources on first load into Python bytecode for best runtime performance.
4. Easy to debug with a debug system that integrates template compile and runtime errors into the standard Python traceback system.
5. ...

## Installation
```
pip install Jinja2
```

## Tutorial
Intro: https://www.fullstackpython.com/jinja2.html
Flask Example: https://realpython.com/blog/python/primer-on-jinja-templating/
Template Intro: http://jinja.pocoo.org/docs/2.9/templates/#line-statements

## Basic API Usage
1. Python API
```
>>> from jinja2 import Template
>>> template = Template('Hello {{ name }}!')
>>> template.render(name='Hongwei Hu')
'Hello Hongwei Hu!'

>>> t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
>>> t.render()
'My favorite numbers: 1 2 3 4 5 6 7 8 9 '
```
By creating an instance of Template you get back a new template object that provides a method called render() which when called with a dict or keyword arguments expands the template. The dict or keywords arguments passed to the template are the so-called “context” of the template.

2. Basic 
Jinja2 uses a central object called the template Environment. Instances of this class are used to store the configuration and global objects, and are used to load templates from the file system or other locations. Even if you are creating templates from strings by using the constructor of Template class, an environment is created automatically for you, albeit a shared one.

Most applications will create one Environment object on application initialization and use that to load templates. In some cases however, it’s useful to have multiple environments side by side, if different configurations are in use.

``` 
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('yourapplication', 'templates'),
    # autoescape=select_autoescape(['html', 'xml'])
    autoescape = True
)
```

This will create a template environment with the default settings and a loader that looks up the templates in the templates folder inside the yourapplication python package. 

``` python
template = env.get_template('cloud.html')
print(template.render(latitude='42', longitude='-71'))

template = env.get_template('template-test.py')
print(template.render(escape='TRUE'))
```

3. https://realpython.com/blog/python/primer-on-jinja-templating/

For those who have not been exposed to a templating language before, such languages essentially contain variables as well as some programming logic, which when evaluated (or rendered into HTML) are replaced with actual values. The variables and/or logic are placed between tags or delimiters.

For example, Jinja templates use {% ... %} for expressions or logic (like for loops), while {{ ... }} are used for outputting the results of an expression or a variable to the end user. 

A Jinja template is simply a text file. Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc.). A Jinja template doesn’t need to have a specific extension: .html, .xml, or any other extension is just fine.

A template contains variables and/or expressions, which get replaced with values when a template is rendered; and tags, which control the logic of the template. The template syntax is heavily inspired by Django and Python.

{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
#  ... ## for Line Statements





