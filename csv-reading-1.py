import csv;

with open("data.txt") as csv_file:
    csv_reader=csv.reader(csv_file);
    for line in csv_reader:
       for word in line:
           print(word,end="\t");
       print("");