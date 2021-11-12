import cfg
import vk_api
import datetime # работа с датой и временем
import time

botvk = cfg.tokenvk

vkwork=0
class pusk:
    def pc():
        global vkwork
        vkwork = 1
        ntime=0
        global botvk
        while vkwork==1:
            try:
                vk = vk_api.VkApi(token=botvk)
                delta = datetime.timedelta(hours=3, minutes=0)  # разница от UTC. Можете вписать любое значение вместо 3
                t = (datetime.datetime.now(datetime.timezone.utc) + delta)  # Присваиваем дату и время переменной «t»
                nowtime = t.strftime("%H:%M")  # текущее время
                nowdate = t.strftime("%d.%m.%Y")  # текущая дата
                ntime=ntime+1
                n=str(ntime)
                vk.method("status.set", {"text": nowtime + " ● " + nowdate + " ● " + n + " ● "})
                time.sleep(30)  # погружаем скрипт в «сон» на 30 секунд
            except:
                time.sleep(20)

    def ost():
        global vkwork, botvk
        vkwork = 0
        try:
            vk = vk_api.VkApi(token=botvk)
            vk.method("status.set", {"text": "Оффлайн"})
        except:
            time.sleep(20)
            ost()
