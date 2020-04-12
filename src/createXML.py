import dicttoxml

def create_xml(input_filename, output_filename, dataset):
    # Arguments
    black_list = {"ISIN","Country","Currency","Exchange","Quantity","C_Gain_Loss"}
    annexs = {"Rosto":"","AnexoA":"","AnexoJ" : ["Quadro08","Quadro09"]}
   
    #annexs = ["Rosto","AnexoA","AnexoJ"]
    #tables = ["Quadro01","Quadro02","Quadro03","Quadro04","Quadro05","Quadro06","Quadro07","Quadro08","Quadro09","Quadro10","Quadro11"]
    
    new_dictiory = {}
     
# read dictionary dataset
    print(dataset.items())

# select the needed information from parse
    for key ,val in dataset.items():
        new_dataset={}
        for k ,v in val.items():
            new_dataset_values = {k:v for (k,v) in v.items() if k not in black_list}
            new_dataset.update({k:[new_dataset_values]})
        print(new_dataset)

# Create a new dictionary: enter information as required by the IRS

    x = 3   
    #for i in annexs:
    for key, value in annexs.items(): 
        for v in value:
        #new_table_line = {}
        #for j in tables:
            new_line = {}
            for k in range(1,x) :
                new_line.update({"AnexoJq092AT01-Linha numero="+str(k):"abc"})
                new_dic_line = {v: new_line}
                new_dictiory.update(new_dic_line)
            #new_dic_table = {i:new_dic_line}
            #new_dictiory.update(new_dic_table)
    print(new_dictiory)

    IRS = {
        "NLinha" : "",
	    "CodPais" : "",
	    "Codigo" : "",
	    "AnoRealizacao" : "",
	    "MesRealizacao" : "",
	    "ValorRealizacao" : "",
	    "AnoAquisicao" : "",
	    "MesAquisicao" : "",
	    "ValorAquisicao" : "",
	    "DespesasEncargos" : "",
	    "ImpostoPagoNoEstrangeiro" : "",
	    "CodPaisContraparte" : ""
        }

    # Transformar em XML
    xml_snippet = dicttoxml.dicttoxml(new_dataset, root=False)    

    #Escrever em ficheiro
    with open( "tmp.xml", "w") as f:
        f.write(str(xml_snippet))


example = {
    "j_9p2_a": {
         "0" : {
            "ISIN" : "LU0599900635",
            "Type" : "G20",
            "Country" : "442",
            "Currency" : "EUR",
            "Exchange" : "1,00000",
            "Quantity" : "0,26",
            "A_Date" : "22.05.2019",
            "A_Value" : "27,00",
            "S_Date"  : "24.06.2019",
            "S_Value"  : "27,18",
            "T_Costs" : "0,00",
            "C_Gain_Loss" : "0,18",
            "Tax" : "0.00",
            "Counterparty_C" : "442"
        },
            "1" : {
            "ISIN" : "LU0599900635",
            "Type" : "G20",
            "Country" : "442",
            "Currency" : "EUR",
            "Exchange" : "1,00000",
            "Quantity" : "0,01",
            "A_Date" : "17.06.2019",
            "A_Value" : "0,61",
            "S_Date"  : "24.06.2019",
            "S_Value"  : "0,61",
            "T_Costs" : "0,00",
            "C_Gain_Loss" : "-0,00",
            "Tax" : "0.00",
            "Counterparty_C" : "442"
        },
            # "2" : {
            # "ISIN" : "LU0599900635",
            # "Type" : "G20",
            # "Country" : "442",
            # "Currency" : "EUR",
            # "Exchange" : "1,00000",
            # "Quantity" : "0,02",
            # "A_Date" : "17.06.2019",
            # "A_Value" : "2,50",
            # "S_Date"  : "24.06.2019",
            # "S_Value"  : "2,51",
            # "T_Costs" : "0,00",
            # "C_Gain_Loss" : "0,01",
            # "Tax" : "0.00",
            # "Counterparty_C" : "442"
        # }
    }
}
create_xml("documents/bla.xml", "output.xml" , example )