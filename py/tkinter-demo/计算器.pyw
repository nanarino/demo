import tkinter
from decimal import Decimal
from typing import Union
from re import sub
root = tkinter.Tk()
root.geometry('280x500')
root.resizable(0,0)
root.title('计算器') 
main_screen = tkinter.StringVar()
main_screen.set('0')
history_screen = tkinter.StringVar()
history_screen.set('')
label = tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',fg = '#828282',anchor = 'se',textvariable = history_screen)
label.place(width = 280,height = 170)
label2 = tkinter.Label(root,font = ('微软雅黑',30),bg = '#EEE9E9',bd ='9',fg = 'black',anchor = 'se',textvariable = main_screen)
label2.place(y = 170,width = 280,height = 65)  
btn7 = tkinter.Button(root,text = '7',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : onclick('7'))
btn7.place(x = 0,y = 285,width = 70,height = 55)
btn8 = tkinter.Button(root,text = '8',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : onclick('8'))
btn8.place(x = 70,y = 285,width = 70,height = 55)
btn9 = tkinter.Button(root,text = '9',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : onclick('9'))
btn9.place(x = 140,y = 285,width = 70,height = 55)
btn4 = tkinter.Button(root,text = '4',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : onclick('4'))
btn4.place(x = 0,y = 340,width = 70,height = 55)
btn5 = tkinter.Button(root,text = '5',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : onclick('5'))
btn5.place(x = 70,y = 340,width = 70,height = 55)
btn6 = tkinter.Button(root,text = '6',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : onclick('6'))
btn6.place(x = 140,y = 340,width = 70,height = 55) 
btn1 = tkinter.Button(root,text = '1',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : onclick('1'))
btn1.place(x = 0,y = 395,width = 70,height = 55)
btn2 = tkinter.Button(root,text = '2',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : onclick('2'))
btn2.place(x = 70,y = 395,width = 70,height = 55)
btn3 = tkinter.Button(root,text = '3',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : onclick('3'))
btn3.place(x = 140,y = 395,width = 70,height = 55)
btn0 = tkinter.Button(root,text = '0',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : onclick('0'))
btn0.place(x = 70,y = 450,width = 70,height = 55)
btnpoint = tkinter.Button(root,text = '.',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:onclick('.'))
btnpoint.place(x = 140,y = 450,width = 70,height = 55)
btnac = tkinter.Button(root,text = 'AC',bd = 0.5,font = ('黑体',20),fg = 'orange',command = lambda :onclick('AC'))
btnac.place(x = 0,y = 230,width = 70,height = 55)
btnback = tkinter.Button(root,text = '←',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:onclick('←'))
btnback.place(x = 70,y = 230,width = 70,height = 55)
btndivi = tkinter.Button(root,text = '÷',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:onclick('÷'))
btndivi.place(x = 140,y = 230,width = 70,height = 55)
btnmul = tkinter.Button(root,text ='×',font = ('微软雅黑',20),fg = "#4F4F4F",bd = 0.5,command = lambda:onclick('×'))
btnmul.place(x = 210,y = 230,width = 70,height = 55)
btnsub = tkinter.Button(root,text = '-',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:onclick('－'))
btnsub.place(x = 210,y = 285,width = 70,height = 55)
btnadd = tkinter.Button(root,text = '+',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:onclick('＋'))
btnadd.place(x = 210,y = 340,width = 70,height = 55)
btnequ = tkinter.Button(root,text = '=',bg = 'orange',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :equal_onclick())
btnequ.place(x = 210,y = 395,width = 70,height = 110)
btnper = tkinter.Button(root,text = '%',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:onclick('%'))
btnper.place(x = 0,y = 450,width = 70,height = 55)
is_error = 1
def brief_num(n:Union[int, float, Decimal]):
    return '{:.8g}'.format(float(n))
def computed(numA:str,numB:str,sym:str):
    if sym == '＋':
        return Decimal(numA) + Decimal(numB)
    elif sym == '－':
        return Decimal(numA) - Decimal(numB)
    elif sym == '×':
        return Decimal(numA) * Decimal(numB)
    elif sym == '÷':
        return Decimal(numA) / Decimal(numB)
    else :
        return Decimal(0)
def evaluation(arr:list[str]):
    arr = arr[:]
    multiplication_list = list(filter((lambda z : z == '×' or z == '÷'),arr))  
    addition_list = list(filter((lambda z : z == '＋'or z == '－'),arr))
    while 1:
        try:
            first = multiplication_list.pop(0)
        except:
            try:
                first = addition_list.pop(0)
            except:           
                break
        idx = arr.index(first)
        res = computed(arr[idx-1],arr[idx+1],sym=first)
        arr[idx-1:idx+2]=[res]
    return arr.pop(0)
def onclick(target:str):
    global is_error
    if is_error:
        if target =='←':
            main_screen.set(str(main_screen.get())[0:-1])
        elif target =='%':
            history_screen.set(str(main_screen.get())+'×100%') 
            try:
                main_screen.set(brief_num(Decimal(main_screen.get())*100)+'%')
            except:
                is_error = 0
                main_screen.set("ERROR")
        elif target !='AC':                                
            main_screen_value = str(main_screen.get())           
            if target.isdecimal() and main_screen_value =='0':    
                main_screen.set(target)
            else:
                main_screen.set(main_screen_value + target)
    if target =='AC':
        main_screen.set("0")
        history_screen.set("")
        is_error = 1
def equal_onclick():
    history_screen.set(str(main_screen.get()))
    eq = sub(r'(?P<sym>[＋－×÷])', lambda _: f',{_.group("sym")},', main_screen.get())
    if eq[0] == ',':
        eq = '0' + eq
    try:
        result = brief_num(evaluation(arr=eq.split(',')))
    except Exception:
        global is_error
        is_error = 0
        result = "ERROR"
    main_screen.set(result) 
root.mainloop()
