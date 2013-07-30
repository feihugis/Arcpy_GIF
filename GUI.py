#encoding:utf-8
import Tkinter
import FileDialog 
import FieldOperation
import ExportMap
import xlrd
import arcpy
from PIL import Image, ImageSequence
import sys, os
from images2gif import writeGif

#生成打开文件对话框
def OpenArcFile( Event ):
	global ArcFile
	fd = FileDialog.LoadFileDialog( root )
	ArcFile = fd.go()
	Text_1.insert(1.0, ArcFile)
	print ArcFile

def OpenExcelFile( Event ):
	global ExcelFile
	fd = FileDialog.LoadFileDialog( root )
	ExcelFile = fd.go()
	Text_2.insert(1.0, ExcelFile)
	print ExcelFile

def OpenMxdFile( ):
	global MxdFile
	fd = FileDialog.LoadFileDialog( root )
	MxdFile = fd.go()
	Text_mxd.insert(1.0, MxdFile)
	print MxdFile

def Process( ):
	"""
	Fieldname = 'Other'
	Unionname = 'FID'
	ArcFile = r'C:\Users\Hu Fei\Desktop\Data\BloomfieldTownship\SchoolTaxDistrict.shp'
	ExcelFile = r'C:\Users\Hu Fei\Desktop\Data\data1.xls'
	MxdFile = r'E:\GitHub\Arcpy_GIF\Data\Test.mxd'
	OutputFolder = r'C:\Users\Hu Fei\Desktop\Data'
    """
	Fieldname = entry_field.get()
	Unionname = entry_union.get()
	OutputFolder = entry_output.get()
	
	excel = xlrd.open_workbook( ExcelFile)
	num_sheet = excel.nsheets
	GIF_name = []
	for ii in xrange(0,num_sheet):
		  FieldOperation.Add_Field_Name( ArcFile, Fieldname, "DOUBLE")
		  FieldOperation.Update_Field_Value(ArcFile, ExcelFile,ii , Unionname, Fieldname)
		  out_put = OutputFolder + '\\' + str(ii) + '.gif'
		  GIF_name.append(out_put)
		  ExportMap.Change_GraduatedValuesSymbology( MxdFile, r"C:\Users\Hu Fei\Desktop\Data\Temp.lyr", Fieldname, out_put)
	ExportMap.Make_Animated_Gif( GIF_name, OutputFolder+'\Animated_GIF.gif')



 
#点击关闭按钮后： 
def eBtnClose( ):
    root.destroy()


 #定义文件名
filename = ''
ArcFile = ''
ExcelFile = ''
MxdFile = ''
 #所有界面的鼻祖
root = Tkinter.Tk(className="数据更新与动态GIF合成")

root.geometry("600x440+200+200") #在xy轴200-200的位置创建400*220的窗口
 
#开始写界面显示部份：
#直到使用Tkinter.Frame布局之前，界面完全是一塌糊涂
line_1 = Tkinter.Frame(root)
l_1 = Tkinter.Label(line_1,text="Shape文件路径:",width="20")
Text_1 = Tkinter.Text(line_1, height = 1, width = "35")
btnArc = Tkinter.Button(line_1,text="打开",width="10")
btnArc.bind('<Button-1>',OpenArcFile)#绑定按钮事件
l_1.pack(side = "left",pady = 8)
Text_1.pack(side = "left")
line_1.pack(side = "top",fill = "x")
btnArc.pack(side="left",padx = 20)
 
line_2 = Tkinter.Frame(root)
l_2 = Tkinter.Label(line_2,text="Excel文件路径",width="20")
Text_2 = Tkinter.Text(line_2, height = 1, width = 35)
btnExcel = Tkinter.Button(line_2,text="打开",width="10")
btnExcel.bind('<Button-1>',OpenExcelFile)#绑定按钮事件
l_2.pack(side = "left",pady = 8)
Text_2.pack(side = "left")
line_2.pack(side = "top",fill = "x")
btnExcel.pack(side="left",padx = 20)

line_mxd = Tkinter.Frame(root)
l_mxd = Tkinter.Label(line_mxd,text="Mxd文件路径:",width="20")
Text_mxd = Tkinter.Text(line_mxd, height = 1, width = "35")
btnMxd = Tkinter.Button(line_mxd,text="打开",width="10", command = OpenMxdFile)
l_mxd.pack(side = "left",pady = 8)
Text_mxd.pack(side = "left")
line_mxd.pack(side = "top",fill = "x")
btnMxd.pack(side="left",padx = 20)
 
line_3 = Tkinter.Frame(root)
l_3 = Tkinter.Label(line_3,text="输出文件路径",width="20")
entry_output = Tkinter.Entry(line_3,width="40")
l_3.pack(side = "left",pady = 8)
entry_output.pack(side = "left")
line_3.pack(side = "top",fill = "x")

line_union = Tkinter.Frame(root)
l_union = Tkinter.Label(line_union,text="链接字段",width="20")
entry_union = Tkinter.Entry(line_union,width="40")
l_union.pack(side = "left",pady = 8)
entry_union.pack(side = "left")
line_union.pack(side = "top",fill = "x")
 
line_field = Tkinter.Frame(root)
l_field = Tkinter.Label(line_field,text="添加字段",width="20")
entry_field = Tkinter.Entry(line_field,width="40")
l_field.pack(side = "left",pady = 8)
entry_field.pack(side = "left")
line_field.pack(side = "top",fill = "x")


line_btn = Tkinter.Frame(root)
btnLogin = Tkinter.Button(line_btn,text="更新字段并出图", command = Process, width = 20)
btnClose = Tkinter.Button(line_btn,text="关闭", command = eBtnClose, width = 20)
line_btn.pack(side = 'top', fill = "x", pady = 10)
btnLogin.pack(side="left",padx = 50)
btnClose.pack(side = 'left', padx = 30)

#终于把界面显示部份写完了

root.mainloop()
