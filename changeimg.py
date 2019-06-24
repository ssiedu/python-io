f=open("e:\\images\\mymobile.png","rb");
res=f.read();
f.close();
f1=open("g:\\testimg\mobilecopy.png","ab");
f1.write(res);
f1.close();
print("completed");