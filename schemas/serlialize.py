def serializeDict(item) -> dict:
    return {**{i:str(item[i]) for i in item if i =='_id'}, **{i:item[i] for i in item if i !='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]