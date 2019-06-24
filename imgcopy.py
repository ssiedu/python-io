f1=open("g:\\testimg\\mobilecopy.png","rb");
res=f1.read();
f1.close();


f2=open("g:\\testimg\mobile1.png","wb");
f2.write(res);
f2.close();
print("copy successfully completed");

