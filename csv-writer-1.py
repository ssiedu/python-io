import csv;

with open("data.txt","a") as csv_file:
    csv_writer=csv.writer(csv_file);
    
    row=["prakash","sql","ratlam"];
    csv_writer.writerow(row);
    
    
    

print("Completed");