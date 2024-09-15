import json
import os
import numpy as np
import csv

FindFor = 'atom_plddts'
FindForIPTM = 'iptm'
FindForPTM = 'ptm'

def find_json_files(directory):
    json_files = []
    for file in os.listdir(directory):
        if file.endswith('.json'):
            json_files.append(os.path.join(directory, file))
    return json_files

current_directory = os.path.dirname(os.path.abspath(__file__))
files = find_json_files(current_directory)

plddt_header = ['File', 'plDDT']
plddt = []
misc_header = ['File', 'iPTM', 'pTM']
misc = []

for file in files:
    with open(file) as f:
        d = json.load(f)

        if FindFor in d:
            avg = np.array(d[FindFor]).mean()
            print(file, ', Average pLDDT: ', avg)
            plddt.append([os.path.basename(file), avg])

        iptmvalue = d.get(FindForIPTM, None)
        ptmvalue = d.get(FindForPTM, None)
        
        if iptmvalue is not None or ptmvalue is not None:
            misc.append([os.path.basename(file), iptmvalue, ptmvalue])
            if iptmvalue is not None:
                print(file, ', IPTM value: ', iptmvalue)
            if ptmvalue is not None:
                print(file, ', PTM value: ', ptmvalue)

with open('plddt.csv', 'w') as file_writer:
    writer = csv.writer(file_writer)
    writer.writerow(plddt_header) 
    for item in plddt:
        writer.writerow(item)

with open('ptmiptm.csv', 'w') as file_writer:
    writer = csv.writer(file_writer)
    writer.writerow(misc_header)  
    for item in misc:
        writer.writerow(item)
