#Paolo Poemape

import os
import re

MINI_CORE_DIR = "/Users/paolopoemape/Desktop/Mini-CORE_new/"
for register in ["HI", "ID", "IN", "IP", "LY", "NA", "OP", "SP"]:
    count_all = 0
    count1, count2, count3 = 0, 0, 0
    for child_file in os.listdir(MINI_CORE_DIR):
        if child_file[2:4] == register:
            with open(MINI_CORE_DIR + child_file, encoding ='CP437') as infile:
                whole_file_as_str = infile.read().lower()
                whole_file_as_str = re.sub(r"<.*?", "", whole_file_as_str)
                wds = re.split(r"[^-''a-z]", whole_file_as_str, flags=re.IGNORECASE)
                for wd in wds:
                    count_all += 1
                    if re.search(r"\w", wd, flags=re.IGNORECASE):
                        count1 += 1
                    if re.search(r"\w+", wd, flags=re.IGNORECASE):
                        count2 += 1
                    if re.search(r"\w", wd, flags=re.IGNORECASE):
                        count3 += 1

    norm1 = (count1 / count_all) * 1000
    print(norm1)
norm2 = count2 / count_all * 1000
norm3 = count3 / count_all * 1000
