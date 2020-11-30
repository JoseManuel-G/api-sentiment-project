from config.configuration import db, collection

def mensaje_person(nombre):
    query = {'name': f'{nombre}'}
    frases =  list(collection.find(query, {'name': 1, 'line': 1, '_id': 0}))
    return frases


def mensajes():
    mensaje =  list(collection.find({},{'_id':0}))
    return mensaje
