""" using urlLIB to read a web page
"""

import urllib

from urllib import request
d = dir(urllib)
resp = request.urlopen('https://www.wikipedia.org')
print(resp.peek())

print('hi')

