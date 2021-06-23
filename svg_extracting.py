from svgpathtools import svg2paths
from svg.path import parse_path
from svg.path.path import Line


from xml.dom import minidom

doc = minidom.parse('dragon.svg')
path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]

doc.unlink()

print(path_strings)
