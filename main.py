import pyautogui
import time
import pyperclip

#python
#pyautogui.hotkey("alt", "tab")

filenames = ['numbers.txt', 'names.txt']

def gen_line(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

gens = [gen_line(n) for n in filenames]

for file1_line, file2_line in zip(*gens):
    #print("\t".join([file1_line, file2_line]))
    #print(file1_line)
    #print(file2_line)
    pyautogui.click(x = 1738, y = 110)
    pyautogui.click(x = 969, y = 432)
    pyautogui.typewrite(file1_line)
    pyautogui.click(x = 1248, y = 436)
    pyautogui.click(x = 948, y = 1166)
    pyautogui.typewrite(f"Hi {file2_line}. This is Afrox. We are hiring for the role of Solderer/Repair Operator in Milpitas, CA")
    pyautogui.press("Enter")




