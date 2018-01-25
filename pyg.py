# pip install pygments
# python pyg.py code_file
# takes in a python code_file and generates an html
# display-friendly version of the python file. 

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

import sys

code_file = sys.argv[1]
output_name = code_file.split(".")[0]
output_html = output_name + ".html"
output_css = output_name + ".css"

f_in = open(sys.argv[1], "r")

code = f_in.read()

f_out_html = open(output_html, "w")
f_out_css = open(output_css, "w")

head = '''
<head>
  <link rel="stylesheet" href="''' + output_css + '''">
</head>
'''

f_out_html.write(head)
f_out_html.write(highlight(code, PythonLexer(), HtmlFormatter()))

f_out_css.write(HtmlFormatter().get_style_defs('.highlight'))
