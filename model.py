from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from natasha import AddrExtractor, MorphVocab
import re

tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-large-finetuned-conll03-german")
model = AutoModelForTokenClassification.from_pretrained("xlm-roberta-large-finetuned-conll03-german")
classifier = pipeline("ner", model=model, tokenizer=tokenizer)

def findEmail(text):
    array_email = []
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    for email in emails:
        array_email.append(email)
    return array_email

def findNumber(text):
    array_phone_number = [
        numbers.group()
        for numbers in re.finditer(r"((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}", text)
        ]
    return array_phone_number

def findTegOrg(result):
    orgName = []
    for k in result:
      if k["entity"] == "I-ORG" or k["entity"] == "I-PER":
        orgName.append(k["word"])
    orgNameStr = ''.join(orgName).replace('▁', ' ')
    return orgNameStr

def findAddr(text):
    addres = []
    addrStr = ''
    morph_vocab = MorphVocab()
    addr_extractor = AddrExtractor(morph_vocab)
    result = addr_extractor.find(text)
    for addr in result.fact.parts:
        addres.append(addr.type)
        addres.append(addr.value)
    for _ in addres:
        addrStr += str(_) + " "
    return addrStr

def findDopInfo(result):
    dopInfo = []
    for k in result:
        if k["entity"] != "I-ORG":
            if k["entity"] != "I-LOC":
                if k["entity"] != "I-PER":
                    dopInfo.append(k["word"])
    dopInfoStr = ''.join(dopInfo).replace('▁', ' ')
    if len(dopInfoStr) == 0:
        dopInfoStr = "Дополнительных данных нет"
        return dopInfoStr
    else:
        return dopInfoStr

# text = input()
# result = classifier(text) #Оюработка названия
# orgName = findTegOrg(result)
# print(orgName)