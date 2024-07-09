import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login/")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=647, y=370)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("arturvictorsm@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")
pyautogui.click(x=819, y=528)

base = pd.read_csv("produtos.csv")

for i in base.index:
    pyautogui.click(x=777, y=245)
    pyautogui.write(str(base.loc[i, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(base.loc[i, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(base.loc[i, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(base.loc[i, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(base.loc[i, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(base.loc[i, "custo"]))
    pyautogui.press("tab")
    if str(base.loc[i, "obs"]) != "nan":
        pyautogui.write(str(base.loc[i, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("pageup")