import os
import docx

#leer partes
"""
doc = docx.Document("demo.docx")

#cantidad de párrafos en el documento
print(len(doc.paragraphs))

#el texto de un párrafo especifico
print(doc.paragraphs[1].text)

#cuantos runs hay un parrafo especifico
print(len(doc.paragraphs[1].runs))

#un run esp dentro de un párrafo esp
print(doc.paragraphs[1].runs[0].text)
"""

#leer todo

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText("demo.docx"))