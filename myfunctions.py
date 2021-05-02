#--LISTS--

def remove_duplicates(lista):
    output = []
    [output.append(x) for x in lista if x not in output]
    return output

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

#--JSON--
def write_json(contenido,archivo):
    with open(archivo,"w",encoding="utf-8") as f:
        out=json.dumps(contenido,indent=4)
        f.write(out)