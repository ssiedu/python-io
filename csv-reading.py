f=open("data.txt");
print("___________________________________");
for line in f:
    res=line.split(",");
    for item in res : 
        print(item,end="\t");
    print("");

print("___________________________________");