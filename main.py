import os
from tqdm import tqdm, trange 
import time
import math

columns, lines = os.get_terminal_size()
maxwidth = columns

print("Terminal size:", columns, "columns x", lines, "lines")


# DFH - Dotted Full Heavy
# DFM - Dotted Full Medium
# DFL - Dotted Full Light
# Full, Left, Right, Top, Bottom, DFH, DFM, DFL
ASCII_OBJECTS = [chr(9608), chr(9612), chr(9616), chr(9600), chr(9604), chr(9619), chr(9618), chr(9617)]
ASCII_OBJECTS_IDs = [[9608, 0, 'Full'], [9612, 1, 'Left'], [9616, 2, 'Right'], [9600, 3, 'Top'], [9604, 4, 'Bottom'], [9619, 5, 'DFH'], [9618, 6, 'DFM'], [9617, 7, 'DFL']]

print(ASCII_OBJECTS)

def ap(c, r) -> str:
    global maxwidth
    if r > maxwidth:  return '|' + math.ceil((int(maxwidth)-23)/2)*chr(9633) + ' Text Aera Too Small ' + math.floor((int(maxwidth)-23)/2)*chr(9633) + '|'
    for superitem in ASCII_OBJECTS_IDs:
        for item in superitem:
            if c == item:
                return chr(superitem[0]) * int(r)
    if r >= 3:
        return '|' + math.ceil((int(r)-17)/2)*chr(9633) + ' CHR Not Found ' + math.floor((int(r)-17)/2)*chr(9633) + '|' 
    elif r == 2: 
        return '||'
    elif r <= 1: 
        return chr(9633) * r

pbar = tqdm(total=100)
for i in range(10):
    time.sleep(0.1)
    pbar.update(10)
pbar.close()

print('done')

print(ap('DFM', 216))
# import pyfiglet
# T = input("Enter Text you want to convert to ASCII art : ")
# ASCII_art_1 = pyfiglet.figlet_format(T)
# print(ASCII_art_1)