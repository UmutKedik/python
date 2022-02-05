import os
import re
import glob
import pandas as pd

# file directory for txt files
path = "Enter the folder you want to extract the ip address"

# file directory for excel save path
excel_save_path = "Enter the folder directory you want to save as excel"

# IP address regex pattern
pattern = re.compile(r'(?:(?:1\d\d|2[0-5][0-5]|2[0-4]\d|0?[1-9]\d|0?0?\d)\.){3}(?:1\d\d|2[0-5][0-5]|2[0-4]'
                     r'\d|0?[1-9]\d|0?0?\d)')

# creating 2 list for valid IP and invalid IP
valid = []
invalid = []

# using glob module to take all txt files in directory
for path in glob.glob(os.path.join(path, "*.txt")):
    with open(path, mode="r", encoding="utf-8") as fh:
        string = fh.readlines()

    # search all data inside of the file for our IP regex pattern
    for line in string:
        line = line.rstrip()
        result = pattern.search(line)

        # valid IP addresses
        if result:
            valid.append(line)

        # invalid IP addresses
        else:
            invalid.append(line)

# displaying the IP addresses
print("Valid IPs")
print(valid)
print("Invalid IPs")
print(invalid)

# sorting IP adresses from low to high
valid.sort(key=str)

# deleting same IPs
valid = list(dict.fromkeys(valid))

# converting list to dataframe type for writing to the excel
df = pd.DataFrame(valid)

# changing the column name to IP_LIST  for more understandable word
df = df.rename(columns={0: 'IP_LIST'})

# saving to excel using pandas
df.to_excel('{}/IP_list.xlsx'.format(excel_save_path))
