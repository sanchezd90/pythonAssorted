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
    def getIds(self):
        idString=re.split("IdList",self.response().content.decode('UTF-8'))[1][1:-2]
        return [self.stripIdElement(x) for x in idString.split("\n")][1:-1]
    def getData(self,*args):
        results=[]
        for id in self.getIds():
            f=Fetch(id)
            results.append(f.get(*args))
        return results
    def saveData(self,*args):
        results=[]
        for id in self.getIds():
            f=Fetch(id)
            results.append(f.get(*args))        
        with open(f"{self.term}.json","w",encoding="utf-8") as f:
            f.write(json.dumps(results,indent=4))

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
    def get(self,*args):
        data=self.toDict()["pmc-articleset"]["article"]        
        fieldDict= {}
        for arg in args:
            #--- ALL ---#
            if arg == "all":
                try:
                    fieldDict["journal-title"]=data["front"]["journal-meta"]["journal-title-group"]["journal-title"]
                except Exception as e:
                    fieldDict["journal-title"]="notFound"
                    print(f"Error in '{arg}' search ",e)
            
                try:
                    for ids in data["front"]["article-meta"]["article-id"]:
                            if ids["@pub-id-type"]=="doi":
                                fieldDict["doi"]=ids["#text"]
                except Exception as e:
                    fieldDict["doi"]="notFound"
                    print(f"Error in '{arg}' search ",e)
            
                try:
                    fieldDict["title"]=data["front"]["article-meta"]["title-group"]["article-title"]
                except Exception as e:
                    fieldDict["title"]="notFound"
                    print(f"Error in '{arg}' search ",e)
           
                try:                    
                    fieldDict["date"]=data["front"]["article-meta"]["pub-date"][0]
                except Exception as e:
                    fieldDict["date"]="notFound"
                    print(f"Error in '{arg}' search ",e)
            
                try:
                    fieldDict["abstract"]=data["front"]["article-meta"]["abstract"]["p"]["#text"]
                except Exception as e:
                    fieldDict["abstract"]="notFound"
                    print(f"Error in '{arg}' search ",e)
           
                try:
                    fieldDict["keywords"]=data["front"]["article-meta"]["kwd-group"]["kwd"]
                except Exception as e:
                    fieldDict["keywords"]="notFound"
                    print(f"Error in '{arg}' search ",e)

                return fieldDict 
            #--- JOURNAL TITLE ---#
            elif arg == "journal-title":
                try:
                    fieldDict["journal-title"]=data["front"]["journal-meta"]["journal-title-group"]["journal-title"]
                except Exception as e:
                    fieldDict["journal-title"]="notFound"
                    print(f"Error in '{arg}' search ",e)
            
            #--- DOI ---#
            elif arg == "doi":
                try:
                    for ids in data["front"]["article-meta"]["article-id"]:
                            if ids["@pub-id-type"]=="doi":
                                fieldDict["doi"]=ids["#text"]
                except Exception as e:
                    fieldDict["doi"]="notFound"
                    print(f"Error in '{arg}' search ",e)
            
            #--- TITLE ---#
            elif arg == "title":
                try:
                    fieldDict["title"]=data["front"]["article-meta"]["title-group"]["article-title"]
                except Exception as e:
                    fieldDict["title"]="notFound"
                    print(f"Error in '{arg}' search ",e)
           
            #--- DATE ---#
            elif arg == "date":
                try:                    
                    fieldDict["date"]=data["front"]["article-meta"]["pub-date"][0]
                except Exception as e:
                    fieldDict["date"]="notFound"
                    print(f"Error in '{arg}' search ",e)
            
            #--- ABSTRACT ---#
            elif arg == "abstract":
                try:
                    fieldDict["abstract"]=data["front"]["article-meta"]["abstract"]["p"]["#text"]
                except Exception as e:
                    fieldDict["abstract"]="notFound"
                    print(f"Error in '{arg}' search ",e)
            
            #--- KEYWORDS ---#
            elif arg == "keywords":
                try:
                    fieldDict["keywords"]=data["front"]["article-meta"]["kwd-group"]["kwd"]
                except Exception as e:
                    fieldDict["keywords"]="notFound"
                    print(f"Error in '{arg}' search ",e)
        return fieldDict



