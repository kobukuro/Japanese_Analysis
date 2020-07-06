import csv
import re
#processed_jap_eng
with open('processed\processed_jap_eng.csv', encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile)
    vocs = []
    for row in rows:
        input = row[0]
        pattern = '.っ.り' #.っ.り
        output = re.search(pattern, input)
        if output != None:
            if len(input) == 4:
                vocs.append(input)
                print(input)
        # break
    print(len(vocs))