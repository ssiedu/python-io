import csv;

data=[{"name":"manoj","city":"dewas"},{"name":"amit","city":"bhopal"},{"name":"yatin","city":"ujjain"}];
fields=["name","city"];

with open("persons.txt","w") as file:
    writer=csv.DictWriter(file,fieldnames=fields);
    writer.writeheader();
    writer.writerows(data);

print("Writing Complete");
