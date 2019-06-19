import os;
import shutil;

res1=os.getcwd(); # gets the current working directory;
print(res1);

res2=os.listdir();# if no paramters are given it gives list of cwd
#print(res2);

res3=os.listdir("g:/python-code"); # it gives the list of elements in given directory
#print(res3);

#res4=os.mkdir("trial");# it creates a new directory and return none raise FileExistsError if already available
#print(res4);

#res5=os.rename("trial","test"); #renames trial to test (can rename a file and directory as well)
#print(res5);

#res6=os.remove("myscript.py");  #removes a file
#print(res6);

#res7=os.rmdir("test");  #removes an empty directory only
#print(res7);

res8=shutil.rmtree("test"); #removes an non-empty directory.
print(res8);
