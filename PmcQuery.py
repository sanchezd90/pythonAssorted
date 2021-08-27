import requests
import re
import xmltodict
import json

class Search():
    
    def __init__(self,term,field="title",tool="my_tool",email="my_email@example.com",search_url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term="):
        
        self.term=term.strip()
        self.field=field.strip().lower()
        self.tool=tool.strip()
        self.email=email.strip()
        self.search_url=search_url.strip()
        

    def url(self):
        return f"""{self.search_url}{self.term.replace(" ","+")}%5B{self.field}%5D&tool={self.tool}&email={self.email}"""                    
    def response(self):
        return requests.get(self.url())
    def stripIdElement(self,idElement):
        return idElement.strip("<Id>").strip("</Id>")    
    def idList(self):
        idString=re.split("IdList",self.response().content.decode('UTF-8'))[1][1:-2]
        return [self.stripIdElement(x) for x in idString.split("\n")][1:-1]    

class Fetch():

    def __init__(self,id,tool="my_tool",email="my_email@example.com",fetch_url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id="):

        self.id=id.strip()        
        self.tool=tool.strip()
        self.email=email.strip()
        self.fetch_url=fetch_url.strip()

    def url(self):
        return f"""{self.fetch_url}{self.id}&tool={self.tool}&email={self.email}"""    

    def response(self):
        return requests.get(self.url())
    def toJson(self):
        return json.dumps(xmltodict.parse(self.response().content), indent=4)
    def save(self):
        with open(f"{self.id}.json","w",encoding="utf-8") as f:
            f.write(self.toJson())
    def toDict(self):
        return json.loads(self.toJson())

