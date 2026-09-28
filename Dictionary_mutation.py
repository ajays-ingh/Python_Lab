def add_entry(d):
    d["age"] = 19

dict = {"name": "Ajay"}
print("Before function call:", dict)
add_entry(dict)
print("After function call:", dict)    


def reassign_dict(d):
    d = {"city": "Ranchi"}

dict = {"name": "Ajay"}
print("Before function call:", dict)
reassign_dict(dict)
print("After function call:", dict)