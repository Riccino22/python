import json  

def add_to_json(filename, data):  
    try:
        with open(filename, "r") as file:  
            info = json.load(file)
    except json.decoder.JSONDecodeError:
        info = []
    
    info.append(data)
    
    for index, item in enumerate(info):  
        item["id"] = index + 1  
        
    with open(filename, "w") as file:  
        json.dump(info, file, indent=4)

def get_json(filename):
    try:
        with open(filename, "r") as file:  
            info = json.load(file)
    except json.decoder.JSONDecodeError:
        info = []
    return info