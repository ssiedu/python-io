f=open("g:/pythondata/data.txt","rb");
print(f.read(5));
print(f.tell());
print(f.seek(8,1));
print(f.tell());
print(f.read(4));