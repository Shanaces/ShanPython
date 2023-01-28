#Dictionary
#dictionary uses curly braces
#Unordered,changable, indexed, no duplicates
Dict1={
    "Brand": "Tecno",
    "Model": "Techno camon 12",
    "Model": "Techno camon 9",
    "Year of Manufacture":1989
}
print(Dict1)
#accessing the items
print(Dict1["Brand"])
print(Dict1["Year of Manufacture"])
print(Dict1["Model"])

#changing/update the model
Dict1["Model"]="Techno Camon 9"
print(Dict1)

Dict2={
    "Brand":"Subaru",
    "Model":["Impreza","Forester","Outback"],
    "YOM":2000
}
print(Dict2)
print(Dict2["Model"])
print(type(Dict2["Model"]))
print(type(Dict2["Brand"]))
print(type(Dict2["YOM"]))
