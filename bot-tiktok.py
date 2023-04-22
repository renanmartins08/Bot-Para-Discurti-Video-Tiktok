import webbrowser #permite usar o navegador
import pyautogui # vai permitir simular o  mouse
from time import sleep # vai permitir esperar enquantas acontece os carregamento da pagina


#- entra na conta tik-tok
webbrowser.open('https://www.tiktok.com/')
sleep(10)
#- clica no perfil da conta perfil da conta 
pyautogui.click(1327,101,duration=2)
sleep(3)
#click em visualizar perfil
pyautogui.click(1323,152,duration=2)
sleep(5)
#- navegar ate curtidas 
pyautogui.click(472,406,duration=2)
sleep(10)
#- selecinar um video
pyautogui.click(355,603,duration=2)
sleep(5)

#-click no coração para descurtir
#-descurtir quanta vezes você precisar
for video in range(50):
        #-click no coração para descurtir
        imagem = pyautogui.locateCenterOnScreen('img/coracao.png')
        if imagem:
                pyautogui.moveTo(imagem,duration =2)
                pyautogui.leftClick()
                sleep(3)
#passa para poximo video       
        else:
            pyautogui.press('down')
            sleep(5)


