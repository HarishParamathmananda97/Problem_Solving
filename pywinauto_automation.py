from pywinauto.application import Application

app = Application().start(r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.exe')

#describe the window inside Notepad.exe process
dlg_spec = app.window(title="Untitled - Notepad")

#wait till the window is really open
actionable_dlg = dlg_spec.wait('visible')

#bringing to foreground
actionable_dlg.set_focus()



#to stop the started program
app.kill()
#ERD_CAREF_EB - EP_FACTENTRY - WinSCP

from subprocess import Popen
from pywinauto import Desktop

Popen('calc.exe', shell=True)
dlg = Desktop(backend="uia").Calculator
dlg.wait('visible')

# can be multi-level
app.window(title_re='.* - Notepad$').window(class_name='Edit')

dlg = Desktop(backend="uia").Calculator
dlg.set_focus()
dlg.window(auto_id="num8Button'", control_type="Button")

