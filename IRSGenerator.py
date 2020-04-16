#import camelot
#import PyPDF2
import re
import xml.etree.ElementTree as ET
import src.createXML as createXML
import src.parsePDF as parsePDF
import argparse

# convert PDF into CSV file


class IRSgenerator():
    
    def __init__(self):
        pass
        #parsePDF()
       
         #create_xml(example)




#Executed as a script

#irs = IRSgenerator()

data  = parsePDF.parsePDF()
createXML.create_xml("src/irs_original.xml", "irs.xml" , data.dict)
# Inicializacao - IRSgenerator
# Input - les ficheiros e trasmorfas em python datasets 
# Parsing - transformas os datasets em algo q queiras
# Output

