"""
data.py
---------------------------------------------------------------------------
- This file contains all the data you'd like to be converted to a FZP file.
- Please do not change any variable names as it will break the main code.
- If you have any questions, please go to
---------------------------------------------------------------------------
"""

"""Libraries - DO NOT TOUCH ANYTHING HERE"""

from datetime import date


"""Constants - DO NOT TOUCH ANY VARIABLES HERE"""

today = date.today()

"""Script Mode"""

#interactive  = False ### True/False. If true, run the main code straight away. If false, please fill in the data here
#professional = False ### True/False. If true, fzp file will pass the top parts standards.

"""Section A - Main Data"""

filename        = "fritzing_part.fzp"
fritzingVersion = "1.0.6" ### x.x.x
moduleId        = "part_module_id_1"

title   = "Part name"
version = "1"
author  = "RAPTOR7762"
date    = today.isoformat()
label   = "A"
family  = "Solar Panel" ## Give the part's family name
variant = "Variant 1" ## Give the part's variant name
layer   = "?" ### Try not to leave the following fields blank. If you do not know, leave it as "?". 
mn      = "?" ### You can always remove it later in Fritzing.
mpn     = "?"
partNo  = "?"

tags       = ["fritzing user", "contrib", "tag3", "tag4"] ### Add as many as you want!
properties = [["NA", "NA"], ["NA2", "NA2"]] ### Use the format: [[property1, instance1], [property2, instance2]]

description = '''&lt;html>
&lt;p>Give this part a good description!&lt;/p>
&lt;p>HTML or Plain Text. &lt;strong>Bold&lt;/strong>, &lt;em>italic&lt;/em>.&lt;/p>
&lt;p>Remember to escape &amp;!&lt;/p>&lt;/html>'''

"""Section B - Views"""

bbImg   = "xxx.svg" ### Breadboard View Image. Leave blank like this "" to disable view.
schImg  = "xxx.svg" ### Schematic View Image. Leave blank like this "" to disable view.
pcbImg  = "xxx.svg" ### PCB View Image. Leave blank like this "" to disable view.
iconImg = "xxx.svg" ### Icon View Image. Leave blank like this "" to disable view/sync view.

# Advanced #

noPCB        = False
noSchematic  = False
noBreadboard = False
THT          = True

### Danger: ONLY one True among the following statements (under construction)

#iconSameAsBB  = True
#iconSameAsSCH = False
#iconSameAsPCB = False

"""Section C - Connectors"""

noOfCons = 2 ### No. of connectors

# Advanced

bendableLegs = False
allMale      = True