# opening a file
f=open("g:\\pythondata\\info.txt");
# reading a file
"""
result1=f.read();    # reads the complete file and returns us a string
print(type(result1));
print(result1);
"""

"""
result2=f.readline();   #reads line by line and returns a string of length zero after reading last line.
print(type(result2));
print(result2);
print(len(f.readline()));
print(len(f.readline()));
print(len(f.readline()));
print(len(f.readline()));
print(len(f.readline()));
print(len(f.readline()));
"""

"""
result3=f.readlines();  #reads the complete file and returns the list of strings each line is one element of list
print(type(result3));

for line in result3:
    print(line);
"""

"""
result4=f.read(6);  #reads the only 6 characters and pointer moves to 7th
print(result4);
"""

for line in f:      #directly reading the file using for loop (line by line)
    print(line);





f.close();


