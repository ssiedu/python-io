#f=open("g:/pythondata/info.txt");   #opening file without with


with open("g:/pythondata/info.txt") as f :                  #opening file using with (automatically close the file out of with block)
    print(f.read());


#f.close();          #closing file (if we open it using with we dont need to close it)

print(f.closed);    #check and return true if file is closed otherwise false
