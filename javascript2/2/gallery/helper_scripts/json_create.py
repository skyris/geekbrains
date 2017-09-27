import json


lst = []
for i in range(1, 22):
    d = {}
    d["path"] =      "img{:03}_{}_{}.jpeg".format(i, 1200, 800)    
    d["thumbPath"] = "img{:03}_{}_{}.jpeg".format(i, 300, 200)    
    d["desc"] = ""
    lst.append(d)    

with open("pictures.json", "w") as fd: 
    fd.write(json.dumps(lst, indent=4))
