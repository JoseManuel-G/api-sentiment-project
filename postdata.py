from config.configuration import db,collection

def insertamensaje(name_episode,name,frase): 
    dict_insert = {
    "episode name": f"{name_episode}",
    "name": f"{name}",
    "line": f"{frase}",
    }
    while dict_insert not in list(collection.find({}, {'name': 1,'episode name':1, 'line': 1, '_id': 0})):
        collection.insert_one(dict_insert)