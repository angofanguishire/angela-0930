import spacy
import json
from fastapi import FastAPI


app = FastAPI()



@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/ner/{text}")
def ner(text: str):

    # process entered text
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # map each detected word with its entity
    dict={}
    for entity in doc.ents:
        dict[entity.text]=entity.label_
    
    # Visualize the processed text
    str_list=list(text.split())
    for i in range(len(str_list)):
        if str_list[i] in dict:
            str_list[i] = '\['+ str_list[i] + '\]' + '\(' + dict[str_list[i]] + '\)' 
    
    # obtain NER processed string
    ner_str=" ".join(str(word) for word in str_list)
    print("processed string", ner_str)
    ner_dict={}
    ner_dict["result"]=ner_str

    # create json object to send to Wave app
    json_object=json.dumps(ner_dict, indent=4)

    return json_object




