import dicttoxml

def create_xml(input_filename, output_filename, dataset):
    # Arguments
    black_list = {"ISIN","Country","Currency","Exchange","Quantity","C_Gain_Loss"}
    rename     = {"Country":"CodPais"}
    anexos = ["Rosto","AnexoA","AnexoJ"]
    quadros = ["Quadro01","Quadro02","Quadro03","Quadro04","Quadro05","Quadro06","Quadro07","Quadro08","Quadro09","Quadro10","Quadro11"]
   
    # Ola
    new_dictiory = {}
    
     
    #print(dataset.items())
    #=new_example = {k:v for k,v in abc.iteritems() if k not in black_list_values}
    ## se usares um for vais buscar as coisas

    # ler o dicionario dataset (exemplo)
    # ir buscar informacao necessaria (parse)
    new_dataset = {rename.get(key,key) : val for key ,val in dataset.items()}
    for key ,val in dataset.items():
        for k ,v in val.items():
            new_dataset = {rename.get(kk,kk) : vv for kk ,vv in v.items()}
            #print(new_dataset)

    # criar novo dicionario 
    # Introduzir informacao como e requerida para o IRS
    x = 5
    for anaxo in anexos:
        new_quadro_line = {}
        for i in range(0,x) :
            new_quadro_line.update({"AnexoJq092AT01-Linha_"+str(i) : "asd"})
        new_dic_line = {anaxo: new_quadro_line}
        new_dictiory.update(new_dic_line)
    
    print(new_dictiory)

    # Transformar em XML
    xml_snippet = dicttoxml.dicttoxml(new_dataset, root=False)    

    #Escrever em ficheiro
    with open( "tmp.xml", "w") as f:
        f.write(str(xml_snippet))


newExample ={
    "Ane"
        "nii"
        "CodPais"
}


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
            "2" : {
            "ISIN" : "LU0599900635",
            "Type" : "G20",
            "Country" : "442",
            "Currency" : "EUR",
            "Exchange" : "1,00000",
            "Quantity" : "0,02",
            "A_Date" : "17.06.2019",
            "A_Value" : "2,50",
            "S_Date"  : "24.06.2019",
            "S_Value"  : "2,51",
            "T_Costs" : "0,00",
            "C_Gain_Loss" : "0,01",
            "Tax" : "0.00",
            "Counterparty_C" : "442"
        }
    }
}
create_xml("documents/bla.xml", "output.xml" , example )
