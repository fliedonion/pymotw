__author__ = 'takahiro'
import textwrap
from textwrap_example import simple_text

dedented_text = textwrap.dedent(simple_text).strip()
print textwrap.fill(dedented_text, initial_indent='', subsequent_indent='    ')
