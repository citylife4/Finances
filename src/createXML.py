import dicttoxml
import xml
import xmltodict

def create_xml(input_filename, output_filename, dataset):
# Arguments
    black_list = {"ISIN","Currency","Exchange","Quantity","C_Gain_Loss"}

# select the needed information from parse
    for key ,val in dataset.items():
        new_dataset={}
        for k ,v in val.items():
            new_dataset_values = {k:v for (k,v) in v.items() if k not in black_list}
            new_dataset.update({k:new_dataset_values})

# Create a new dictionary
    x = int(list(new_dataset.keys())[-1]) + 2
    list1=[]
    for i in range(1,x) :
        line = str(i-1)
        dict1 = {
            "@numero": str(i),
            "NLinha" : str(int(i+950)),
            "CodPais" : new_dataset[line]['Country'],
            "Codigo" : new_dataset[line]['Type'],
            "AnoRealizacao" : new_dataset[line]['S_Date'][6:10],
            "MesRealizacao" : str(int(new_dataset[line]['S_Date'][3:5])),
            "ValorRealizacao" : new_dataset[line]['S_Value'].replace(',','.'),
            "AnoAquisicao" : new_dataset[line]['A_Date'][6:10],
            "MesAquisicao" : str(int(new_dataset[line]['A_Date'][3:5])),
            "ValorAquisicao" : new_dataset[line]['A_Value'].replace(',','.'),
            "DespesasEncargos" : new_dataset[line]['T_Costs'].replace(',','.'),
            "ImpostoPagoNoEstrangeiro" : new_dataset[line]['Tax'],
            "CodPaisContraparte" : new_dataset[line]['Counterparty_C'].replace(',','.')
            }
        list1.append(dict1)

# Enter information as required by the IRS
    with open(input_filename, "r") as fd:
        irs_dict =xmltodict.parse(fd.read())
    irs_dict['Modelo3IRSv2020']['AnexoJ']['Quadro09']['AnexoJq092AT01']['AnexoJq092AT01-Linha'] = list1

   
# Transform to XML and write to a file
    print(xmltodict.unparse(irs_dict, pretty=True))
    with open(output_filename, "w") as outfile:
        outfile.write(xmltodict.unparse(irs_dict, pretty=True))
