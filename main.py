import pyautogui
import time
import random

time.sleep(2)


# cria duas coordenadas e clica no ponto dado pelas coordenadas
def criarponto():
    y = random.randint(176, 227)
    x = random.randint(473, 552)
    print(x, y)
    pyautogui.click(x, y)


# retorna x e y da pos atual do mouse
def coordenadas():
    cordx, cordy = pyautogui.position()
    return cordx, cordy


# desenha o num de linhas especificados
def desenharlinhas(num):
    pyautogui.click(15, 269)  # clica na ferramenta polilinhas
    criarponto()  # cria o ponto inicial
    criarponto()  # cria segundo ponto da linha
    pyautogui.press('enter')  # encerra com enter
    ult_x, ult_y = pyautogui.position()
    pyautogui.rightClick()
    cx, cy = pyautogui.center(
        pyautogui.locateOnScreen('copiar.png',
                                 region=(452, 165, 402, 342)))  # vai ate a opcao copiar

    pyautogui.click(cx, cy)  # clica na opcao copiar
    pyautogui.rightClick()  # clica com o botao direito pra procurar a opcao colar
    time.sleep(2)
    print("achado em: ", pyautogui.center(pyautogui.locateOnScreen('colar.png')))
    cox, coy = pyautogui.center(pyautogui.locateOnScreen('colar.png'))  # vai ate a opcao colar
    pyautogui.click(cox, coy)  # clica na opcao colar
    pyautogui.click(17, 135)   # ferramenta de selecao
    pyautogui.click(ult_x, ult_y)  # volta ao ultimo traco feito
    pyautogui.doubleClick(60, 87)  # clica pra alterar a coordanada e mover o traco
    pyautogui.write('2,5')  # move ate 3,57cm da pagina
    pyautogui.doubleClick(64, 105)  # faz o mesmo com a altura
    pyautogui.write('22,8')  # move ate 21cm de altura da pagina
    pyautogui.click(15, 269)  # volta para a ferramenta de selecao
    pyautogui.moveTo(ult_x, ult_y)  # move de volta ao ultimo ponto criado
    locais_tracos = (("18,5","17,9"), ("2,5","13"), ("2,5","8"))
    # loop para criar pontos conectados com o anterior
    for a in range(num - 1):
        print('iteracao: ', a)
        codx, cody = coordenadas()
        print("x e y:", codx, cody)
        pyautogui.click(17, 135)  # ferramenta selecao
        pyautogui.click(281, 261)  # ponto qualquer
        pyautogui.click(15, 269)  # ferramenta polilinhas
        pyautogui.click(codx, cody)  # clica no fim da linha anterior
        criarponto()  # cria nova linha a partir do fim da anterior
        pyautogui.press('enter')  # encerra nova linha com enter
        time.sleep(1)  # aguarda 1s para pegar melhores valores do random

        ult_x, ult_y = pyautogui.position()
        pyautogui.rightClick()
        cx, cy = pyautogui.center(
            pyautogui.locateOnScreen('copiar.png',
                                     region=(452, 165, 402, 342)))  # vai ate a opcao copiar

        pyautogui.click(cx, cy)  # clica na opcao copiar
        pyautogui.rightClick()  # clica com o botao direito pra procurar a opcao colar
        time.sleep(2)
        cox, coy = pyautogui.center(pyautogui.locateOnScreen('colar.png'))  # vai ate a opcao colar
        pyautogui.click(cox, coy)  # clica na opcao colar
        pyautogui.click(17, 135)  # ferramenta de selecao
        pyautogui.click(ult_x, ult_y)  # volta ao ultimo traco feito
        pyautogui.doubleClick(60, 87)  # clica pra alterar a coordanada e mover o traco
        pyautogui.write(locais_tracos[a][0])  # move ate Xcm da pagina
        pyautogui.doubleClick(64, 105)  # faz o mesmo com a altura
        pyautogui.write(locais_tracos[a][1])  # move ate Xcm de altura da pagina
        pyautogui.click(15, 269)  # volta para a ferramenta de selecao
        pyautogui.moveTo(ult_x, ult_y)  # move de volta ao ultimo ponto criado

# Escreve o texto passado por um arquivo txt nos campos requisitados
def escrevertexto():
    texto = "Nam sollicitudin risus a arcu euismod, non congue ante euismod. Aenean scelerisque cursus lobortis. Aliquam blandit vestibulum tempor. Nunc ut molestie ante. Vivamus eget dictum tortor. Integer at tincidunt elit. Proin at aliquet turpis. In pharetra orci eu turpis venenatis varius quis quis felis. Duis et enim nibh. Nullam suscipit turpis eget sem sagittis, ut malesuada nunc dapibus. Praesent ex elit, pellentesque sed pharetra non, aliquet non lacus. Quisque vitae varius urna, vitae tempor tortor. Fusce arcu diam, consequat dignissim magna eget, consequat consequat elit. Duis a felis odio. Donec tincidunt purus vitae lacus porta aliquam."
    coord = ((551,281),(468,358),(548,432),(536,509))
    for i in range(4):
        pyautogui.click(15,421) #ferramenta texto
        pyautogui.click(coord[i]) #clica na caixa de texto desejada
        pyautogui.write(texto)

# Move o simbolo inicial criado completo para o fim da pagina
def movesimbolo():
    pyautogui.click(17, 135)  # ferramenta de selecao
    pyautogui.moveTo(472, 174)
    pyautogui.mouseDown()
    pyautogui.moveTo(553, 227)
    pyautogui.mouseUp()
    pyautogui.click(515, 206,button='right')
    time.sleep(2)
    cx, cy = pyautogui.center(
        pyautogui.locateOnScreen('copiar.png',
                                 region=(452, 165, 402, 342)))  # vai ate a opcao copiar

    pyautogui.click(cx, cy)  # clica na opcao copiar
    pyautogui.click(1050, 385)  # oculta caixas de texto
    pyautogui.moveTo(755,360)
    pyautogui.rightClick()  # clica com o botao direito pra procurar a opcao colar
    print("aqui")
    time.sleep(2)
    print("achado em: ", pyautogui.center(pyautogui.locateOnScreen('colar.png')))
    cox, coy = pyautogui.center(pyautogui.locateOnScreen('colar.png'))  # vai ate a opcao colar
    pyautogui.click(cox, coy)  # clica na opcao colar
    pyautogui.doubleClick(60, 87)  # clica pra alterar a coordanada e mover o simbolo
    pyautogui.write('10,5')  # move ate Xcm da pagina
    pyautogui.doubleClick(64, 105)  # faz o mesmo com a altura
    pyautogui.write('1,97')  # move ate Xcm de altura da pagina


desenharlinhas(4)
pyautogui.click(1048,385) # mostra as caixas de texto
escrevertexto()
time.sleep(20)
movesimbolo()
pyautogui.click(1047,457) # mostra as caixas de texto
pyautogui.press('enter')  # encerra com enter