import re
import functions


def cab_text(paper):
    with open(paper, 'r') as text:
        data = text.read()
        data = data.replace('..', '')
        data = data.replace('\n', '. ')
        data = data.replace('No.', 'No')
        data = data.replace(' &apos;', '')
        data = data.replace('&apos;', '\'')
        data = data.replace('Hon.', 'Hon')
        data = data.replace('.]', '.] ')
        data = data.replace('.(', '. (')
        data = data.replace('\'\'', '"')
        data = re.sub(r'(\w\.)(\w{2,})', r'\1 \2', data)
        data = re.sub(r'(\))(\w)', r'\1 \2', data)
        data = re.sub(r'([a-z])([A-Z])', r'\1 \2', data)
        data = re.sub(r'([A-Z])\.', r'\1', data)
        data = re.sub(r'\.([a-zA-Z])', r'. \1', data)
        data = re.sub(r',([a-zA-Z])', r', \1', data)
        data = re.sub(r'([0-9],)([a-zA-Z])', r'\1, \2', data)
        data = re.sub(r'([a-z])([0-9])', r'\1 \2', data)
    return data


cab_paper = cab_text('cab/CAB_23_1_0_0040.txt')

print(cab_paper)

print(functions.summarize(cab_paper, 1, False, 110))
