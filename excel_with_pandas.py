import pandas as pd
import yargy_services as ys
import model as md
from natasha import AddrExtractor, MorphVocab
from datetime import datetime
start_time = datetime.now()

data = pd.read_excel('try.xlsx', header=None)

'''
findOrgName - функция для поиска тегов названий в строчке. Сначала строчка проходит токенизацию,
а потом модель по этим токенам ставит тег. 
Данная функция забирает теги I-ORG и I-PER с расчетом на то, что во многих названиях фигурируют имена собственные.
'''
def findOrgName(text):
    result = md.classifier(text)  # Обработка названия
    orgName = md.findTegOrg(result)
    if len(orgName) == 0:
        return "Название найти не удалось"
    else:
        return orgName


'''
findEmail - с помощью регулярного выражения из строчки забирает email
'''
def findEmail(text):
    email = md.findEmail(text)
    if len(email) == 0:
        return "Почта не указана"
    else:
        return email


'''
findNumber - с помощью регулярного выражения из строчки забирает номер телефона
'''
def findNumber(text):
    number = md.findNumber(text)  # Обработка номера
    if len(number) == 0:
        return "Номер телефона не указан"
    else:
        return number


'''
findDopInfo - функция для доп информации. Принимает все остальные теги от модели, чтобы не упустить что-то важное из строчки
'''
def findDopInfo(text):
    dopInfo = md.findDopInfo(result)  # обработка дополнительной информации
    if len(dopInfo) == 0:
        return "Нет дополнительной информации"
    else:
        return dopInfo


'''
findServices - функция, которая благодаря yargy - parser забирает услуги клиник на основе ранее настроенного правила в services.py
'''
def findServices(text):
    services = ys.findServices(text)  # Обработка услуг лпу
    if len(services) == 0:
        return "Услуги не указаны"
    else:
        return services


'''
findAddr - функция на основе фреймворка Natasha забирает адрес на основе правила на поиск адресов
'''
def findAddr(text):
    address = []
    addrStr = ''
    morph_vocab = MorphVocab()
    addr_extractor = AddrExtractor(morph_vocab)
    result = addr_extractor.find(text)
    if result:
        for addr in result.fact.parts:
            address.append(addr.type)
            address.append(addr.value)
        for _ in address:
            addrStr += str(_) + " "
        return addrStr
    else:
        return ""


'''
Далее формируется датафрейм через pandas, в который, далее, будет записываться результат работы программы
'''
result = pd.DataFrame()
result['raw_data'] = data.iloc[:, 0]


'''
Далее идет записывание в только что сформированный датафрейм, через обрабтку ошибок try catch
'''
try:
    result['LPU'] = result['raw_data'].apply(findOrgName)
    result['address'] = result['raw_data'].apply(findAddr)
    result['email'] = result['raw_data'].apply(findEmail)
    result['number'] = result['raw_data'].apply(findNumber)
    #result['dopInfo'] = result['raw_data'].apply(findDopInfo)
    result['services'] = result['raw_data'].apply(findServices)
except Exception:
    result["Error"] = "Не сработало"


result.to_csv('result.csv', encoding='utf-8') #Сохранение датафрейма
print(datetime.now() - start_time) #Таймер для установки времени работы программы