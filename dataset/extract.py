import sys
import os
import re
from PIL import Image, ImageDraw
import json

def get_cmap():
  # Get the file Mapping
  cmap_filename = 'cmap.json'
  cmap_file = open(cmap_filename, 'r')
  cmap = json.load(cmap_file)
  cmap_file.close()
  return cmap

def write_cmap(cmap):
  cmap_filename = 'cmap.json'
  cmap_file = open(cmap_filename, 'w')
  cmap_file.write(json.dumps(cmap))
  cmap_file.close()


GLOBAL_LABEL = 0
def get_label(cmap, character_name):
  global GLOBAL_LABEL
  if character_name not in cmap:
    cmap[character_name] = GLOBAL_LABEL
    GLOBAL_LABEL += 1
  return cmap[character_name]

def get_image(filename):
  f = open(filename, 'r')
  x = None
  y = None
  start = False
  img = Image.new( 'RGB', (4392,4868), "black") # create a new black image
  draw = ImageDraw.Draw(img)

  for line in f:
    if 'CHARACTER_NAME:' in line:
      character_name = line[len('CHARACTER_NAME:'):].replace(' ', '').rstrip()
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
        draw.line((int(l[0]), int(l[1]), x, y), fill=255, width=80) 
      x = int(l[0])
      y = int(l[1])
  #img.show()
  return character_name, img


cmap = get_cmap()
LISTFILES = open('LISTFILES.txt', 'w')
for folder in range(1, 46):
  dir = 'W' + str(folder)
  for file in os.listdir(dir):
    character_name, img = get_image(dir + '/' + file)
    label = get_label(cmap, character_name)
    output_filename = dir + '/' + character_name + '.jpg'
    LISTFILES.write(output_filename + ' ' + str(label) + '\n')
    print(dir + '/' + file + ': ' + character_name + ' - ' + str(label))
    img.save(output_filename, 'JPEG')
write_cmap(cmap)
LISTFILES.close()
