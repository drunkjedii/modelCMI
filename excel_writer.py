import openpyxl
import yargy_services as ys
import model as md
from datetime import datetime
start_time = datetime.now()

wb = openpyxl.load_workbook(filename='try.xlsx')

data_col = 'A'
sheet = wb.active
cell_range_to_execute = sheet[data_col]
cell_range_OrgNames = sheet['B']
cell_range_Addres = sheet['C']

counter = 1
counter_check = 0

for text in cell_range_to_execute:
    try:
        # if text.value == ' ':
        #     sheet[f'H{counter}'] = "Пусто"
        #     wb.save('try.xlsx')
        #     continue

        result = md.classifier(text.value)  # Обработка названия
        orgName = md.findTegOrg(result)
        if len(orgName) != 0:
            sheet[f'B{counter}'] = orgName
        else:
            sheet[f'B{counter}'] = 'Название организации найти не удалось'

        addres = md.findAddr(text.value)  # Обработка адреса
        if len(addres) != 0:
            sheet[f'C{counter}'] = addres
        else:
            sheet[f'C{counter}'] = 'Адрес найти не удалось'

        email = md.findEmail(text.value)  # Обработка имейла
        if len(email) != 0:
            sheet[f'D{counter}'] = email
        else:
            sheet[f'D{counter}'] = 'Почта не указана'

        number = md.findNumber(text.value)  # Обработка номера
        if len(number) != 0:
            sheet[f'E{counter}'] = number
        else:
            sheet[f'E{counter}'] = 'Номер не указан'

        dopInfo = md.findDopInfo(result)  # обработка дополнительной информации
        if len(dopInfo) != 0:
            sheet[f'F{counter}'] = dopInfo
        else:
            sheet[f'F{counter}'] = 'Дополнительной информации нет'

        services = ys.findServices(text.value)  # Обработка услуг лпу
        if len(services) != 0:
            sheet[f'G{counter}'] = services
        else:
            sheet[f'G{counter}'] = 'Услуг нет'


        counter += 1
        wb.save('try.xlsx')
    except:
        sheet[f'H{counter}'] = "попало в обработку ошибки"
        counter += 1
        wb.save('try.xlsx')
        continue

    # except ValueError:
    #     counter += 1
    #     sheet[f'G{counter}'] = "не сработало"
    #     wb.save('try.xlsx')
    #     continue
    # if text.value == " ":
    #     counter += 1
    #     counter_check += 1
    # else:
    #     result = md.classifier(text.value)  # Обработка названия
    #     orgName = md.findTegOrg(result)
    #     if len(orgName) != 0:
    #         sheet[f'B{counter}'] = orgName
    #     else:
    #         sheet[f'B{counter}'] = 'Название организации найти не удалось'
    #
    #     addres = md.findAddr(text.value)  # Обработка адреса
    #     if len(addres) != 0:
    #         sheet[f'C{counter}'] = addres
    #     else:
    #         sheet[f'C{counter}'] = 'Адрес найти не удалось'
    #
    #     email = md.findEmail(text.value)  # Обработка имейла
    #     if len(email) != 0:
    #         sheet[f'D{counter}'] = email
    #     else:
    #         sheet[f'D{counter}'] = 'Почта не указана'
    #
    #     number = md.findNumber(text.value)  # Обработка номера
    #     if len(number) != 0:
    #         sheet[f'E{counter}'] = number
    #     else:
    #         sheet[f'E{counter}'] = 'Номер не указан'
    #
    #     dopInfo = md.findDopInfo(result)  # обработка дополнительной информации
    #     if len(dopInfo) != 0:
    #         sheet[f'F{counter}'] = dopInfo
    #     else:
    #         sheet[f'F{counter}'] = 'Дополнительной информации нет'
    #
    #     services = ys.findServices(text.value)  # Обработка услуг лпу
    #     if len(services) != 0:
    #         sheet[f'G{counter}'] = services
    #     else:
    #         sheet[f'G{counter}'] = 'Услуг нет'
    #
    #     # except Exception:
    #     #     sheet[f'B{counter}'] = 'Название не найдено'
    #     #     sheet[f'C{counter}'] = 'Адрес не обнаружен'
    #     #     sheet[f'D{counter}'] = 'Почта не указана'
    #     #     sheet[f'F{counter}'] = 'Номер не указан'
    #     #     sheet[f'G{counter}'] = 'Дополнительной информации нет'
    #     #     sheet[f'K{counter}'] = 'Услуг нет'
    #
    #     counter += 1
    #     wb.save('try.xlsx')
    #
    # if counter_check == 10:
    #     wb.save('try.xlsx')
    #     break
    # break

    #wb.save('try.xlsx')

print(datetime.now() - start_time)