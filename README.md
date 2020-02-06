# TokenCreator

Made this token creator to create standing paper tokens for my tabletop games and labels them according to their filename (Note that proper spacing of the label will require [Camel Case](https://simple.wikipedia.org/wiki/CamelCase). See the example .png in the [CreatureImages](/CreatureImages) folder). 

Note that the images will be scaled to the width of the platform base that you provide. The example platform base is 6 inches wide (1 inch = 5 feet ∴ 30 wide or of Colossal size). They can then be scaled down to meet your needs, but if you want to add your own base sized to Medium, Large, Huge, etc, you can do so. If you provide a 1 inch base, you should get token perfect for a single grid square.

Modify the following in token_creator.py file and add folders where necessary:

_img_location = 'YOUR_CREATURE_IMAGE_FOLDER_HERE.png' # The folder that contains the images you want to tokenize.

_img_base_location = 'YOUR_PLATFORM_FOLDER_HERE' # The folder that contains the top and bottom base platform that the token stands on.

_img_platform_top = 'YOU_BASE_PLATFORM_TOP_HERE.png' # The top of circular platform image that the creature will stand on top of. It should sit inside of the _img_base_location folder.

_img_platform_bottom = 'YOU_BASE_PLATFORM_BOTTOM_HERE.png' # The bottom of the circular platform image that the creature will stand on top of. Additionally, the name of the creature .png will be printed on the bottom. It should sit inside of the _img_base_location folder.

_font_folder = 'Fonts' # Note that this is included in the repo, but can be changed. 

_font = 'FFF_Tusj.ttf' # You can change the font by adding a new .ttf to the 'Font' folder and replacing the value of _font to match the new font.

_saveFolder = 'YOUR_SAVE_FOLDER_HERE' # The folder that will contain the newly saved tokens.

**Example:**

<div>
  <img alt="AdamantineGolem.png" src="/CreatureImages/AdamantineGolem.png" width="100"/> 
  <img src="/TokenPlatforms/CharacterBaseTop.png" width="100"/> 
  <img src="/TokenPlatforms/CharacterBaseBottom.png" width="100"/> 
</div>

Creates the following token:

<img src="/SaveFolder/AdamantineGolem.png" width="100"/>
