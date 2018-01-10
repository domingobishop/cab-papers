import re
import functions

with open('cab/CAB_23_1_0_0007.txt', 'r') as text:
    data = text.read().replace('\n', '. ')
    data = data.replace('Hon.', 'Hon')
    data = data.replace('.]', '.] ')
    data = re.sub(r'(\w\.)(\w{2,})', r'\1 \2', data)
    data = re.sub(r'(\))(\w)', r'\1 \2', data)
    data = re.sub(r'([a-z])([A-Z])', r'\1 \2', data)
    data = re.sub(r'([A-Z])\.', r'\1', data)
    data = re.sub(r'\.([a-zA-Z])', r'. \1', data)
    data = re.sub(r',([a-zA-Z])', r', \1', data)

print(functions.summarize(data, 3, False, 300))
