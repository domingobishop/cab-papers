import re
import functions

with open('cab/CAB_23_1_0_0011.txt', 'r') as text:
    data = text.read().replace('\n', '. ')
    data = data.replace('..', '')
    data = data.replace('No.', 'No')
    data = data.replace(' &apos;', '')
    data = data.replace('&apos;', '\'')
    data = data.replace('Hon.', 'Hon')
    data = data.replace('.]', '.] ')
    data = data.replace('.(', '. (')
    data = re.sub(r'(\w\.)(\w{2,})', r'\1 \2', data)
    data = re.sub(r'(\))(\w)', r'\1 \2', data)
    data = re.sub(r'([a-z])([A-Z])', r'\1 \2', data)
    data = re.sub(r'([A-Z])\.', r'\1', data)
    data = re.sub(r'\.([a-zA-Z])', r'. \1', data)
    data = re.sub(r',([a-zA-Z])', r', \1', data)
    data = re.sub(r'([0-9],)([a-zA-Z])', r'\1, \2', data)
    data = re.sub(r'([a-z])([0-9])', r'\1 \2', data)

print(functions.summarize(data, 1, False, 300))
