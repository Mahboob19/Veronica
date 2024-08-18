import eel

import os
from backend.veronica_main import *


eel.init('www')

playInitialSound()
# os.system('start chrome.exe --app-"http://localhost:8000/index.html"')

# eel.start('index.html', mode=None, host='localhost', block=True)

eel.start('index.html')
