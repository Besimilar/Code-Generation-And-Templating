'''
Created on Aug 12, 2017

@author: guangnanliang
'''

from mako.template import Template
from mako.runtime import Context
from io import StringIO

mytemplate = Template("Welcome to ${city}!")
buf = StringIO()
ctx = Context(buf, city="Boston")
mytemplate.render_context(ctx)
print(buf.getvalue())

