import os, sys, time

from datetime import date
from data import *

"""Variables"""



"""File skeleton"""

file = f'''<?xml version='1.0' encoding='UTF-8'?>
<module moduleId="{moduleId}" referenceFile="{filename}" fritzingVersion="{fritzingVersion}">
 <version>{version}</version>
 <author>{author}, fzpgenerator.py</author>
 <title>{title}</title>
 <label>{label}</label>
 <date>{date}</date>
 <tags>
'''

"""Non-professional mode"""

def generatorA():
	global file, tags, properties

	for t in range(len(tags)):
		newTag = f'  <tag>{tags[t]}</tag>\n'

		file += newTag

	file += ' </tags>\n'

	# Properties #

	file += ' <properties>\n'

	file += f'''  <property name="family">{family}</property>
  <property name="variant">{variant}</property>
  <property name="layer">{layer}</property>
  <property name="mn">{mn}</property>
  <property name="mpn">{mpn}</property>
  <property name="part number">{partNo}</property>\n'''

	for p in range(len(properties)):
		newProperty = f'  <property name="{properties[p][0]}">{properties[p][1]}</property>\n'

		file += newProperty

	file += ' </properties>\n'

	# Description #

	file += f' <description>{description}</description>\n'
	
	# Views #

	file += f''' <views>
  <iconView>
   <layers image="breadboard/{iconImg}">
    <layer layerId="icon"/>
   </layers>
  </iconView>
  <breadboardView>
   <layers image="breadboard/{bbImg}">
    <layer layerId="breadboard"/>
   </layers>
  </breadboardView>
  <schematicView>
   <layers image="schematic/{schImg}">
    <layer layerId="schematic"/>
   </layers>
  </schematicView>
  <pcbView>\n'''

	if THT == True:
		file += f'''   <layers image="pcb/{pcbImg}">
    <layer layerId="copper1"/>
    <layer layerId="copper0"/>
    <layer layerId="silkscreen"/>
   </layers>
  </pcbView>
 </views>\n'''

	else:
		file += f'''   <layers image="pcb/{pcbImg}">
    <layer layerId="copper1"/>
    <layer layerId="silkscreen"/>
   </layers>
  </pcbView>
 </views>\n'''

	# Connectors #


#def generatorB():


def saveFile(filename):
	global file

	with open(filename, 'w', encoding='utf-8') as f:
		f.write(file)


def main():
	print('Processing...')
	startTime = time.time()

	generatorA()
	saveFile(filename)

	endTime = time.time()
	elapsedTime = endTime - startTime

	print(f'{elapsedTime:.3f}s')
	print('Done!')

#	else:
#		print('Processing...')
#		generatorB()
#		saveFile(filename)
#		print('Done!')

if __name__ == '__main__':
	main()

"""
except:
	print('\nAn unexpected error occurred. Please check data.py throroughly again.')
	print('If you think you have keyed in all data correctly, please file a bug at:')
	print('')

	sys.exit()
"""