#encoding:utf-8
import Tkinter
 
#点击计算按钮后：
def eBtnDo(event):
 val_1 = entry_1.get()
 val_2 = entry_2.get()
 val_3 = entry_3.get()
 bj = float(val_1)
 yll = float(val_2)
 yll = yll/1000
 yue = float(val_3)
 temp_1 = bj * yll * (1+yll)**yue
 temp_2 = ( (1+yll)**yue - 1)
 result =  temp_1 / temp_2 
 l_result_val.config(l_result_val,text=result)
 
#点击关闭按钮后： 
def eBtnClose(event):
 root.destroy()
 
 #所有界面的鼻祖
root = Tkinter.Tk(className="属性表添加")

root.geometry("800x420+200+200") #在xy轴200-200的位置创建400*220的窗口
 
#开始写界面显示部份：
#直到使用Tkinter.Frame布局之前，界面完全是一塌糊涂
line_1 = Tkinter.Frame(root)
l_1 = Tkinter.Label(line_1,text="贷款本金（元）：",width="20")
entry_1 = Tkinter.Entry(line_1,width="10")
l_1.pack(side = "left",pady = 8)
entry_1.pack(side = "left")
line_1.pack(side = "top",fill = "x")
 
line_2 = Tkinter.Frame(root)
l_2 = Tkinter.Label(line_2,text="月利率（‰）：",width="20")
entry_2 = Tkinter.Entry(line_2,width="10")
l_2.pack(side = "left",pady = 8)
entry_2.pack(side = "left")
line_2.pack(side = "top",fill = "x")
 
line_3 = Tkinter.Frame(root)
l_3 = Tkinter.Label(line_3,text="还款月数（月）",width="20")
entry_3 = Tkinter.Entry(line_3,width="10")
l_3.pack(side = "left",pady = 8)
entry_3.pack(side = "left")
line_3.pack(side = "top",fill = "x")
 
line_result = Tkinter.Frame(root)
l_result = Tkinter.Label(line_result,text="结果",width="20")
l_result_val = Tkinter.Label(line_result,width="80")
l_result.pack(side = "left",pady = 8)
l_result_val.pack(side = "left")
line_result.pack(side = "top",fill = "x")
 
line_btn = Tkinter.Frame(root)
btnLogin = Tkinter.Button(line_btn,text="计算")
btnLogin.bind('<Button-1>',eBtnDo)#绑定按钮事件
btnLogin.pack(side="left")
btnClose = Tkinter.Button(line_btn,text="关闭")
btnClose.bind('<Button-1>',eBtnClose)#绑定按钮事件
btnClose.pack(side="left")
line_btn.pack(side = "top")
#终于把界面显示部份写完了
 
root.mainloop()
