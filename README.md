# Team3

* Hongwei Hu:
    * report: 1-Hongwei_Jinja2.docx
    * video: 
    	* Part1: https://www.screencast.com/t/JV2AfbFVvRpz
    	* Part2: https://www.screencast.com/t/Zf4mpkwrmye
    * presentation: 1-Hongwei_Jinja2.pptx
* Guangnan Liang:
    * report: 
    * presentation:

# Template Engines: 

Material Source: https://www.fullstackpython.com/template-engines.html

Template engines take in tokenized strings and produce rendered strings with values in place of the tokens as output. Templates are typically used as an intermediate format written by developers to programmatically produce one or more desired output formats, commonly HTML, XML or PDF.

## Why are template engines important?
Template engines allow developers to generate desired content types, such as HTML, while using some of the data and programming constructs such as conditionals and for loops to manipulate the output. Template files that are created by developers and then processed by the template engine consist of prewritten markup and template tag blocks where data is inserted.

The template engine would generate the HTML output response when an HTTP request comes in for a particular URL.

## Python template engines
There are several popular Python template engines. A template engine implementation will fall somewhere on the spectrum between allowing arbitrary code execution and granting only a limited set of capabilities via template tags. A rough visual of the code in template spectrum can be seen below for four of the major Python template engines.

![alt text](https://www.fullstackpython.com/img/visuals/template-logic-spectrum.png)

## Jinja (Jinja2)
Jinja, also known and referred to as "Jinja2", is a popular Python template engine written as a self-contained open source project.

Jinja2 is one of the most used template engines for Python. It is inspired by Django's templating system but extends it with an expressive language that gives template authors a more powerful set of tools.

### Tutorial
* Intro: https://www.fullstackpython.com/jinja2.html
* Flask Example: https://realpython.com/blog/python/primer-on-jinja-templating/
* Template Intro: http://jinja.pocoo.org/docs/2.9/templates/#line-statements

## Mako
Mako was the default templating engine for the Pylons web framework and is one of many template engines supported by Pyramid. Mako has wide support as a replacement template engine for many other web frameworks as well.

### Tutorial
* Intro: https://www.fullstackpython.com/mako.html

## Astor
### Tutorial
* Documentation: https://pypi.python.org/pypi/astor
* Tutorial: https://github.com/berkerpeksag/astor

## Cog
### Tutorial
* Documentation: https://www.python.org/about/success/cog/
* Tutorial: https://nedbatchelder.com/code/cog/index.html






