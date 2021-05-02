#--LISTS--

def remove_duplicates(lista):
    output = []
    [output.append(x) for x in lista if x not in output]
    return output

def match_between_lists(listA,listB):
    return any(True if x in listA else False for x in listB)


#--DICTIONARIES--
def replace_dictKey(dictionary,old_key,new_key):
    dictionary[new_key] = dictionary.pop(old_key)

#--PDF-- 

#extracting text from PDF

def extract_one(pdf,page=1):
    if "PyPDF2" not in dir():
        import PyPDF2
    
    with open(pdf, 'rb') as f:
        reader=PyPDF2.PdfFileReader(f)
        page_obj=reader.getPage(page-1)
        return page_obj.extractText()

def extract_range(pdf,start,end):
    if "PyPDF2" not in dir():
        import PyPDF2

    with open(pdf, 'rb') as f:
        reader=PyPDF2.PdfFileReader(f)
        out=""
        for x in range(start-1,end):
            page_obj=reader.getPage(x)
            text=page_obj.extractText()
            out=out+text+"\n"
        return out

#--TEXT FILES--

#write to file
def write_newfile(text,output_file):
    with open(output_file,"w",encoding="utf-8") as f:
        f.write(text)

def txt_to_list(filename):
    lista = []
    with open(filename,"r",encoding="utf-8") as f:
    for entry in f:
        lista.append(entry)
    return lista

#--JSON--
def write_json(contenido,archivo):
    if "json" not in dir():
        import json
    with open(archivo,"w",encoding="utf-8") as f:
        out=json.dumps(contenido,indent=4)
        f.write(out)

def read_json(filename):
    if "json" not in dir():
        import json
    with open(filename,"r",enconding="utf-8") as f:
        content=json.loads(f)
    return content 

#--CSV--
def leercsv(filename):
    contenido = []
    with open(filename,"r") as fin1:
        for num, line in enumerate(fin1):
            if num == 0:
                keys = line.split(";")
            else:
                split = line.split(";")
                d = {}
                for x in range(len(split)):
                    d[keys[x].rstrip("\n")]=split[x].rstrip("\n")
                contenido.append(d)
    return contenido

#--EXCEL--
def get_cell(archivo,cell):
    if "openpyxl" not in dir():
        import openpyxl

    wb = openpyxl.load_workbook(archivo, data_only=True)
    main = wb.sheetnames[0]
    sheet = wb[main]
    return sheet[cell].value
