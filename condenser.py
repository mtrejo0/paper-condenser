import fitz
import json
pdf_document = "pdfs/sample.pdf"
doc = fitz.open(pdf_document)
num_pages = doc.pageCount

print("1 - all\n2 - first & last sentences\n3 - first sentence\n4 - last sentence")
mode = input()


def get_sentences(text):
    text = text.replace("\n", "")
    sentences = text.split(". ")
    sentences = [s.strip() for s in sentences if len(s) > 0]
    return sentences

def get_all():
    condensed = []
    for i in range(num_pages):
        page = doc.loadPage(i)
        blocks = page.getText("blocks")
        for block in blocks:

            text = block[4]
            sentences = get_sentences(text)
            
            condensed.append(sentences)
    return condensed

def get_first_last():
    for i in range(num_pages):
        page = doc.loadPage(i)
        blocks = page.getText("blocks")
        for block in blocks:

            text = block[4]
            sentences = get_sentences(text)

            if len(sentences) > 0:
                group = [sentences[0]]
                if len(sentences) > 2:
                    group.append(sentences[-1])
                condensed.append(group)
    return condensed

def get_first():
    for i in range(num_pages):
        page = doc.loadPage(i)
        blocks = page.getText("blocks")
        for block in blocks:

            text = block[4]
            sentences = get_sentences(text)

            if len(sentences) > 0:
                group = [sentences[0]]
                condensed.append(group)
    return condensed

def get_last():
    for i in range(num_pages):
        page = doc.loadPage(i)
        blocks = page.getText("blocks")
        for block in blocks:

            text = block[4]
            sentences = get_sentences(text)

            if len(sentences) > 0:
                group = [sentences[-1]]
                condensed.append(group)
    return condensed
condensed = []

if mode == "1":
    condensed = get_all()
if mode == "2":
    condensed = get_first_last()
if mode == "3":
    condensed = get_first()
if mode == "4":
    condensed = get_last()


print(json.dumps(condensed, indent = 4))



