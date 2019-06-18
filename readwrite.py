f=open("myfile","r+");
res1=f.read();
print(res1);
f.write("new");
res1=f.read();
print(res1);