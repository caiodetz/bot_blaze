import json
import os
from telebot import TeleBot;
from time import sleep;
from datetime import datetime, timezone, timedelta;
import random;
import requests


# BOT_API_TOKEN = "COLE_O_TOKEN_AQUI"
BOT_API_TOKEN = "7565452007:AAEA5hr4qQd26wEtdGIrhW8Qxk992yqdhz8"
CHANEL_ID = "-1002384265047"
        
os.system("clear")

def GetAllResultsBlaze():    
    try:
        url = "https://blaze.com/api/singleplayer-originals/originals/roulette_games/recent/1"
        headers = {"Host":"blaze.com","Sec-Ch-Ua-Platform":"macOS","Authorization":"Bearer null","Accept-Language":"pt-BR,pt;q=0.9","Sec-Ch-Ua":'"Chromium";v="129", "Not=A?Brand";v="8"',"Sec-Ch-Ua-Mobile":"?0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36","Accept":"application/json, text/plain, */*","X-Client-Version":"v2.2258.0","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://blaze.com/pt/games/double?modal=double_history-v2_index&roomId=1","Accept-Encoding":"gzip, deflate, br","Priority":"u=1, i"}
        res = requests.get(url, headers)
        result = res.json()
        return result
    except:
        Exception("Error ao Buscar ultimos resultados")    

try:
    bot = TeleBot(BOT_API_TOKEN)
except ValueError:
    print("Por gentileza Cole o token do bot na variavel BOT_API_TOKEN")

msg = bot.send_message(CHANEL_ID, "Bot Iniciando")
bot.edit_message_text("Bot Iniciando.", chat_id=CHANEL_ID, message_id=msg.id)
sleep(1);
bot.edit_message_text("Bot Iniciando..", chat_id=CHANEL_ID, message_id=msg.id)
sleep(1);
bot.edit_message_text("Bot Iniciando...", chat_id=CHANEL_ID, message_id=msg.id)
sleep(1);
bot.edit_message_text("✅ Bot Iniciado", chat_id=CHANEL_ID, message_id=msg.id)
sleep(3)
bot.delete_message(CHANEL_ID, msg.id);



colors = ["BRANCO","VERMELHO", "PRETO"]
colors_icons = ["⚪️", "🔴", "⚫️"]

history = []
while True:
    try:
        time_now = datetime.now(timezone(timedelta(hours=-3)));
        HORARIO_ATUAL = f'{time_now.hour}:{time_now.minute:02}'
        print(f'Horrario atual: {HORARIO_ATUAL}')

        
        if time_now.minute % 10 == 0:
            random_minute = random.randint(1, 9)
            # cor = random.randint(0, 2)
            cor = 0
            
            HORARIO_ENTRADA = f'{time_now.hour}:{(time_now.minute + random_minute):02}'
            
            print(f'Horrario da entrada: {HORARIO_ENTRADA}')
            print(f'Cor da entrada: {colors[cor]} - {colors_icons[cor]}')
            
            MESSAGE_TEMPLATE = f"""ENTRE NO {colors_icons[cor]}\n\n⏰ {HORARIO_ENTRADA}"""
            msg = bot.send_message(chat_id=CHANEL_ID,text=MESSAGE_TEMPLATE, timeout=10000)
            history.append(msg)
            
            while time_now.minute % 10 == 0:
                time_now = datetime.now(timezone(timedelta(hours=-3)));
                HORARIO_ATUAL = f'{time_now.hour}:{time_now.minute:02}'
                print(f'Horrario atual: {HORARIO_ATUAL}')
                print("----------------------------------")
                os.system("clear")
            while True:
                time_now = datetime.now(timezone(timedelta(hours=-3)));
                HORARIO_ATUAL = f'{time_now.hour}:{time_now.minute:02}'
                print(f'Horrario atual: {HORARIO_ATUAL}')
                print(f'Aguardando o Horrario do Sinal da Roleta: {HORARIO_ENTRADA}')
                print("----------------------------------")
                sleep(3);
                os.system("clear")
                errors = 0
                if int(HORARIO_ENTRADA.split(":")[1]) == int(HORARIO_ATUAL.split(":")[1]):
                    try:
                        r = GetAllResultsBlaze()
                        HORARIO_ULTIMA_ENTRADA = datetime.fromisoformat(r[0]['created_at'])
                        ULTIMA_ENTRADA_RESULT = colors[r[0]['color']]
                        ENTRADA_SUGERIDA = colors[cor]
                        
                        if ULTIMA_ENTRADA_RESULT == ENTRADA_SUGERIDA:
                            text = f"""✅ 14X do analista""";
                            bot.reply_to(message=msg, text=text)
                            break
                        else:
                            text = f"""❌ Loss""";
                            bot.reply_to(message=msg, text=text)
                            break
                        
                    except:
                        if errors > 3:
                            bot.delete_message(CHANEL_ID, message_id=msg.id)
                            break
                        print("Erro ao Pegar os ultimos resultados da blaze")
                        print("Tentando Novamente")
                        
                        errors += 1
                        
        else:
            print("Aguardando proxima entrada....")
        
        
        
        print("----------------------------------")
        sleep(3)
        os.system("clear")
    except:
        print(f"Messages: {history}")
                
        exit(0)