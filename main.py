import model as md
import yargy_services as ys

text = input()

result = md.classifier(text) #Оюработка названия
orgName = md.findTegOrg(result)
print(f'Название лпу : {orgName}')

addres = md.findAddr(text) #Обработка адреса
print(f'Адрес : {addres}')

email = md.findEmail(text) #Обработка имейла
print(f'Почта : {email}')

number = md.findNumber(text) #Обработка номера
print(f'Номер : {number}')

dopInfo = md.findDopInfo(result) #обработка дополнительной информации
print(f'Дополнительная информация : {dopInfo}')

services = ys.findServices(text) #Обработка услуг лпу
print(f'Услуги ЛПУ : {services}')