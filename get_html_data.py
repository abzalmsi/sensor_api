from bs4 import BeautifulSoup
import requests
import re
import telebot
#######

bot = telebot.TeleBot('5289541830:AAHBQpS0bqtqDT23jhoMy7NkJrEq_xcViDc')
chat_id = "-4036081507"

def get_data(ip, key):
    try:
        url = f"http://{ip}/{key}"     #keys: AKB,V, T, O
        res = requests.get(url, timeout=3)
        soup = BeautifulSoup(res.text, 'html.parser')

        data = soup.find('body').text
        conv_data = re.findall(r'\b\d+\b', data)
        if len(conv_data) > 1:
            data_int = (f'{conv_data[0]}.{conv_data[1]}')
            print(data_int)
            bot.send_message(chat_id, f"IP: {ip} {data_int}")

        else:
            data_int = (conv_data[0])
            print(data_int)
            bot.send_message(chat_id, f"IP: http://{ip}/{key} \nValue: {data_int}")
        return float(data_int)
    except Exception as ex:
        print(f'ОШИБКА: {ex}')
        bot.send_message(chat_id, f"ОШИБКА: \n\n {ex}")
        pass

get_data('10.222.53.38', 'T')