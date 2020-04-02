import tkinter
import subprocess
root = tkinter.Tk()
root.geometry('280x115')
root.resizable(0,0)
root.title('定时关机') 
_entry = tkinter.StringVar()
_entry.set('')
_btn_list = ['设置','取消']
_btn_index = 0
_btn = tkinter.StringVar()
_btn.set(_btn_list[_btn_index])

entry = tkinter.Entry(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd =5,fg = '#828282',textvariable = _entry)
entry.place(width = 100,height = 60)

label = tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd =1,fg = '#828282',anchor = 'se',text = '分钟后关机')
label.place(x=100,width = 180,height = 60)
 
btn = tkinter.Button(root,textvariable = _btn,font = ('微软雅黑',20),bg = '#FAAA3C',bd = 1,activeforeground='#F76832',fg = '#4F4F4F',command = lambda : shutdown_set())
btn.place(x = 0,y = 60,width = 280,height = 55)

def shutdown_set():
    global _btn_index
    if not _btn_index:
        try:
            tim = abs(int(_entry.get())*60)
        except:
            _entry.set('')
            a = subprocess.Popen("shutdown -a", shell=True)
            a.wait()
            _btn_index = int(not bool(_btn_index))
        else:
            _entry.set('')
            if tim == 0:
                return
            a = subprocess.Popen("shutdown -a", shell=True)
            a.wait()
            s = subprocess.Popen("shutdown -s -t "+str(tim), shell=True)
            s.wait()
    else:
        a = subprocess.Popen("shutdown -a", shell=True)
        a.wait()
    _btn_index = int(not bool(_btn_index))
    _btn.set(_btn_list[_btn_index])

root.mainloop()
