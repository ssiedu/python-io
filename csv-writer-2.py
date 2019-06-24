# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:29:17 2019

@author: SSI
"""

import csv;

with open("data.txt","a") as csv_file:
    csv_writer=csv.writer(csv_file);
    
    rows=[["a","b","c"],["d","e","f"],["i","j","k"]];
    csv_writer.writerows(rows);
    
    
    

print("Completed");