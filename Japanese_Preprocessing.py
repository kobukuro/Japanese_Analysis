import glob
import csv
def pre_jap():
    all_vocs = []
    for filename in glob.glob('jap\*.csv'):
         print(filename)
         with open(filename, encoding='utf-8') as csvfile:
             rows = csv.reader(csvfile)
             # ああ言(い)えばこう言(い)う
             for row in rows:
                 if len(row) != 0:
                     this_voc = row[0]
                     if '【' in row[0]:
                         this_voc = this_voc.split('【')[0]
                     if '(' in row[0]:
                         input = True
                         temp = ''
                         for char in row[0]:
                             if char == '(':
                                 input = False
                             if char == ')':
                                 input = True
                                 continue
                             if input:
                                 temp += char
                         this_voc = temp
                     this_voc = this_voc.replace('‐','').replace('・','')
                     if this_voc not in all_vocs:
                         all_vocs.append(this_voc)
         # break
    with open('processed\\processed.csv', 'w', encoding='utf-8') as file:
        for all_voc in all_vocs:
            file.write(all_voc)
            file.write('\n')
def pre_jap_eng():
    all_vocs = []
    for filename in glob.glob('jap_eng\*.csv'):
         print(filename)
         with open(filename, encoding='utf-8') as csvfile:
             rows = csv.reader(csvfile)
             # ああ言(い)えばこう言(い)う
             for row in rows:
                 if len(row) != 0:
                     this_voc = row[0]
                     if '【' in row[0]:
                         this_voc = this_voc.split('【')[0]
                     if '(' in row[0]:
                         input = True
                         temp = ''
                         for char in row[0]:
                             if char == '(':
                                 input = False
                             if char == ')':
                                 input = True
                                 continue
                             if input:
                                 temp += char
                         this_voc = temp
                     this_voc = this_voc.replace('‐','').replace('・','')
                     if this_voc not in all_vocs:
                         all_vocs.append(this_voc)
         # break
    with open('processed\\processed_jap_eng.csv', 'w', encoding='utf-8') as file:
        for all_voc in all_vocs:
            file.write(all_voc)
            file.write('\n')

pre_jap_eng()