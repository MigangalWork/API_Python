import json 

# function to add to JSON
def write_json(data, filename='data.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4)

def update_json(file, new_data, object_name=""):
    with open(file) as json_file: 
        data = json.load(json_file)
        if  object_name!= "":
            data = data[object_name]
        # appending data to emp_details
        data[new_data[0]] = new_data[1]

    write_json(data, file)