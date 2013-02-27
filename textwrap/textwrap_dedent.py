__author__ = 'takahiro'
import textwrap
from textwrap_example import simple_text

dedented_text = textwrap.dedent(simple_text).strip()
print 'Dedent:\n'
print dedented_text


indent = '''
\t    One tab,
\t\tTwo tab,
\tOne tab,
    '''
dedent_text = textwrap.dedent(indent).strip()
print
print dedent_text

