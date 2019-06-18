try:
    x=10;
    f=open("g:/pythondata/info1.txt");
    data=f.read();
    print(data);
except:
    print("some error occured");
finally:
    f.close();
    