

#### EnterDoor G-room-2019-12-23
#### extract information from xml and write into csv. 

import sys
import xml.etree.ElementTree as ET
import csv


#tree = ET.parse("./tmp/z.drug.8049")
inFile = str(sys.argv[1])
#print (inFile)
tree = ET.parse(inFile)

root = tree.getroot()

for drug in root:
    first = drug.find('name').text
    syns = drug.find('synonyms')

    for othernames in syns:
        x1 = othernames.text
        print('#syn\t{}\t{}'.format(first, x1))

    for drugatt in drug.find('products'):

        x2 = drugatt.find('name').text
        x3 = drugatt.find('labeller').text

    tars = drug.find('targets')
    for tar in tars:
        pep = tar.find('polypeptide')
        x4 = pep.find('name').text
        pepsyns = pep.find('synonyms')
        for peps1 in pepsyns:
            x5 = peps1.text
            print ("#target\t{}\t{}\t{}").format(first,x4,x5)

#### ExistDoor of G-room-2019-12-23
