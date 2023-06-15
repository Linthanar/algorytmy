import json

with open('rekurencja_data.json', 'r') as f:
    data = json.load(f)
    search_query = "Lista operatorów"

    def open_file(data):
        for i in data:
            print("     ",i["title"])
            if search_query == i["title"]:
                return 
            for q in i["items"]:
                print(q["title"])
                if search_query == q["title"]:
                    return 
        

    open_file(data)

# print(data)