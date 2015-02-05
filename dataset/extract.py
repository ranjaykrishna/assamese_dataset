import sys
import os
import re
from PIL import Image, ImageDraw

filename = sys.argv[1]
f = open(filename, 'r')
x = None
y = None
start = False
img = Image.new( 'RGB', (4392,4868), "white") # create a new black image
draw = ImageDraw.Draw(img)

for line in f:
  if 'PEN_DOWN' in line:
    start = True
    x = None
    y = None
  if 'PEN_UP' in line:
    start = False
    x = None
    y = None
  if not start:
    continue
  m = re.match(r'[0-9]+ +[0-9]+ +[0-9]+ +[0-9]+\.?', line)
  if m is not None:
    l = str(m.group()).split()
    if x is not None:
      draw.line((int(l[0]), int(l[1]), x, y), fill=0, width=80) 
    x = int(l[0])
    y = int(l[1])
img.thumbnail((50, 50), Image.ANTIALIAS)
img.show()
