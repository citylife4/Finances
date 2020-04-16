#import camelot
#import PyPDF2
import re
import glob
import json
import itertools

class parsePDF():

    def __init__(self, input_folder="documents", doc_name="BancoBest"):

        # Common Variables        
        self.input_pdf_path = input_folder + '/'+ doc_name +'.pdf'
        self.doc_name = doc_name
        self.tmp_folder = 'tmp/'

        #Main class
        #print(self.searchTables())
        #pages_list="3,4,5,6,7,8"
        #pages_list="3,4"
        #print(self.exportJSON(pages_list))
        list_json_all , header_list = self.parseJSONs()
        self.dict = self.createList(list_json_all , header_list)
        


    def searchTables(self, ):
        #Variables
        pages = []
        pages_list=[]

        #Open PDF
        pdfFileObj = open(self.input_pdf_path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)

        #TODO: Maybe change this?
        search_word = "Capital gains/losses on securities|Total Amount"

        # Read PDF and get pages
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            text = pageObj.extractText()
            if re.search(search_word,text):
                pages.append(pageNum)

        #Fail Safe
        if len(pages) != 2:
            print("blaaa")

        #Convert to correct type of string
        for i in range(pages[0]+1,pages[1]+2):
            pages_list.append(str(i))

        return ','.join(pages_list)


    def exportJSON(self, pages_list):
        # Read PDF to tabular
        tabula = camelot.read_pdf(self.input_pdf_path,  pages=pages_list)
        #Convert to JSON
        tmp_input_file_name = self.tmp_folder + self.doc_name + ".json"
        tabula.export(tmp_input_file_name, f = "json")


    def parseJSONs(self):
        tmp_search_json     = self.tmp_folder + self.doc_name + "*.json"
        tmp_ouput_file_name = self.tmp_folder + "temp_" + self.doc_name + ".json"
        tmp_jsons = glob.glob(tmp_search_json)
        list_json_all = []
        header_list = []


        for json_file in tmp_jsons:
            with open(json_file, 'r') as f:
                list_json_all.append(json.load(f))
        
        #print(list_json_all)

        # Check header
        for header in list_json_all[0][0].values():
            header_list.append(header.replace('\n',''))

        #Remove header from json and merge all
        #removed = [ l.pop(0) for l in list_json_all ]
        [ l.pop(0) for l in list_json_all ]
        list_json_all = list(itertools.chain.from_iterable(list_json_all))
        
        #Remvoe last 2
        list_json_all.pop()
        list_json_all.pop()

        #print(header_list)
        #Change the dictionary to have the correct header
        for each_dict in list_json_all:
            #print(each_dict)
            for i, header in enumerate(header_list):
                each_dict[header] = each_dict.pop(str(i))
        
        with open(tmp_ouput_file_name, "w") as write_file:
            json.dump(list_json_all, write_file)

        return list_json_all , header_list

    def createList(self,parsed_json, header_list, board = "j_9p2_a"):
        #[0-9]{1,3}
        tmp_ouput_file_name = self.tmp_folder + "end_" + self.doc_name + ".json"
         
        operation = { 
            "Name ISIN" : re.compile("([A-Z]{2}[A-Z0-9]{9}[0-9]{1})") ,
            "Instrument Type": re.compile("([A-Z]{1}[0-9]{2})") ,
            "Country" : re.compile("([0-9]{1,3})") ,
            "Currency" : re.compile(".*"),
            "Exchange Rate" : re.compile(".*"),
            "Quantity" : re.compile(".*"),
            "Acquisition Date" : re.compile(".*"),
            "Acquisition Value" : re.compile(".*"),
            "Sale Date"  : re.compile(".*"),
            "Sale Value"  : re.compile(".*"),
            "Total Costs" : re.compile(".*"),
            "Capital Gain / Loss" : re.compile(".*"),
            "Withholding Tax" : re.compile(".*"),
            "Counterparty country" : re.compile("([0-9]{1,3})")
        }
        
        new_header = [
            "ISIN" ,
            "Type" ,
            "Country" ,
            "Currency" ,
            "Exchange" ,
            "Quantity" ,
            "A_Date" ,
            "A_Value" ,
            "S_Date"  ,
            "S_Value"  ,
            "T_Costs" ,
            "C_Gain_Loss" ,
            "Tax" ,
            "Counterparty_C" ,
        ]

        new_dictionary = {board : {}}

        for i in range(len(parsed_json)):
            new_dictionary[board].update({str(i):{}})

        for line in new_dictionary[board]:
            for i, keys in enumerate(parsed_json[int(line)]):
                new_line = { new_header[i]:operation[keys].findall(parsed_json[int(line)][keys])[0] }
                new_dictionary[board][line].update(new_line)

        with open(tmp_ouput_file_name, "w") as write_file:
            json.dump(new_dictionary, write_file)     

        return new_dictionary


#parse=parsePDF()
