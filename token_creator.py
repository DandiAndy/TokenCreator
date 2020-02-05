from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import re

_img_location = 'CreatureImages'
_img_base_location = 'TokenPlatforms'
_img_platform_top = 'CharacterBaseTop.png'
_img_platform_bottom = 'CharacterBaseBottom.png'
_font_folder = 'Fonts'
_font = 'FFF_Tusj.ttf'
_saveFolder = 'Pathfinder2eTokens'

_barWidth = 10

def FlipAndStitch(bottom):
  "Copy the image, flip it, then stitch the top and bottom of original and the copy the together. Returns the new stitched image."

  xsize, ysize = bottom.size

  # Flip it!
  top = bottom.crop((0, 0, xsize, ysize))
  top = top.rotate(180)

  # Stitch it!
  stitched = Image.new('RGBA', (xsize, (ysize*2) + _barWidth), (0, 0, 0, 0))
  bar = Image.new('RGBA', (xsize, _barWidth), (0, 0, 0, 255))
  stitched.paste(top, (0, 0))
  stitched.paste(bar, (0, ysize))
  stitched.paste(bottom, (0, _barWidth + ysize))
  
  return stitched;

def AddPlatform(platform_image, token_image):
  "Take the base_image, and split it horizontally through the middle to create a top and bottom-side, the merge the top-side to the top of the token_image and bottom-side to the bottom of the token_image. Returns the full token."

  p_xsize, p_ysize = platform_image.size
  t_xsize, t_ysize = token_image.size

  # We need to scale the image up or down based on the platfrom size (6 inches).
  t_scale = p_xsize / t_xsize
  # t_yscale = p_ysize / t_ysize
  token_xsize = int(round(t_xsize * t_scale))
  token_ysize = int(round(t_ysize * t_scale))
  resized_token_image = token_image.resize((token_xsize, token_ysize))

  top = platform_image.crop((0, 0, p_xsize, p_ysize/2))
  bottom = platform_image.crop((0, p_ysize/2, p_xsize, p_ysize))

  stitched = Image.new('RGBA', (p_xsize, (p_ysize + token_ysize)), (0, 0, 0, 0))
  stitched.paste(top, (0, 0))
  stitched.paste(resized_token_image, (0, top.size[1]))
  stitched.paste(bottom, (0, (token_ysize) + top.size[1]))

  return stitched


def AddTitledBase(base_image, token_image, title):
  "Take the base_image, add the title, and add the titled image to the bottom of the creature token. Returns the full token with a base that can be glued to the bottom."

  b_xsize, b_ysize = base_image.size
  t_xsize, t_ysize = token_image.size

  base_copy = base_image.copy()

  draw = ImageDraw.Draw(base_copy)
  font = ImageFont.truetype(f'{_font_folder}/{_font}', size=50)
  (text_xsize, text_ysize) = font.getsize(title)
  draw.text((int(b_xsize/2 - text_xsize/2), int(b_ysize/2)), title, (0,0,0), font=font)

  stitched = Image.new('RGBA', (b_xsize, (b_ysize + t_ysize)), (0, 0, 0, 0))
  stitched.paste(token_image, (0, 0))
  stitched.paste(base_copy, (0, t_ysize))

  return stitched


platform_image = Image.open(f'{_img_base_location}/{_img_platform_top}')
base_image = Image.open(f'{_img_base_location}/{_img_platform_bottom}')
for filename in os.listdir(_img_location):
  title = re.sub(r"(\w)([A-Z])", r"\1 \2", filename).replace('.png', '')
  creature_image = Image.open(f'{_img_location}/{filename}')
  creature_image = FlipAndStitch(creature_image)
  creature_image = AddPlatform(platform_image, creature_image)
  creature_image = AddTitledBase(base_image, creature_image, title)
  creature_image.save(f'{_saveFolder}/{filename}')
  
  
