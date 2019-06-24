f1=open("g:\\testimg\\mobilecopy.png","rb");
res1=f1.read();
f1.close();


f2=open("g:\\testimg\mobile1.png","rb");
res2=f2.read();
f2.close();

print(len(res1));
print(len(res2));
print(res1==res2);


