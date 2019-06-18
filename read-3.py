f=open("mydata.txt","r");
lines=f.readline();
print(type(lines));
print(lines);
print(f.readline());
f.close();