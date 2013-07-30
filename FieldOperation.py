#coding=utf-8
import arcpy
import csv
import xlrd

def Add_Field_Name( Filename_path, Fieldname_add, Fieldtype_add="DOUBLE", Fieldprecision=15, Fieldscale=5, fieldlength=30, fieldalias="", field_is_nullable="NULLABLE",fiedl_is_required="NON_REQUIRED"):
	  #添加字段
	 arcpy.AddField_management( Filename_path, Fieldname_add, Fieldtype_add, Fieldprecision, Fieldscale, fieldlength, fieldalias, field_is_nullable, fiedl_is_required )

def Delete_Field( Filename_path, Fieldname_delete ):
     #删除字段
     arcpy.DeleteField_management( Filename_path, Fieldname_delete)

def Update_Field_Value( update_table_path, input_table_path,index, Join_field_name, Add_field_name ):
	  #添加字段值
    #打开要添加的数据源
    #reader = csv.reader( open(input_table_path),dialect = 'excel')
    book = xlrd.open_workbook( input_table_path)
    #将数据.csv转入对应的列表中
    data = book.sheet_by_index(index)
    Array_Old = []
    Array_new = []
    for col in range(data.ncols):
          values = []
          for row in range(data.nrows):
              values.append(data.cell(row,col).value)
          print values
          Array_Old.append( values)
    print Array_Old
    row_num = len(Array_Old)
    col_num = len(Array_Old[0])
    print '%d ======%d' %(col_num,row_num)
    for x in xrange(0,col_num):
        Array_new.append([])
        for y in xrange(0,row_num):
            Array_new[x].append(Array_Old[y][x])
    print Array_new
    
    #Join_origine = []
    #cursor_join = arcpy.SearchCursor(Filename)
    #for row in cursor_join:
    #    Join_origine.append( row.getValue(Join_field))
    
    #确定更新数据时连接的field和需要更新的field在列表中的位置
    Join_ID = 0
    Add_ID = 0
    for x in xrange(0, len(Array_new[0])):
        if Array_new[0][x] == Join_field_name:
           Join_ID = x
        if Array_new[0][x] == Add_field_name:
           Add_ID = x
    #将需要使用的连接field和更新field存放在一个字典中
    Add_content = {}
    for x in xrange( 1, len(Array_new) ):
       Add_content[str(Array_new[x][Join_ID])] = Array_new[x][Add_ID]
    print "Update Value is " + str( Add_content )

    
   #根据连接field和更新field来更新update_table
    cursor = arcpy.UpdateCursor(update_table_path)
    row = cursor.next()
    i = 0
    while row:
      ss = float(row.getValue(Join_field_name))
      aa = str(ss)
      print row.getValue(Join_field_name)
      row.setValue(Add_field_name, Add_content[aa])
      cursor.updateRow(row)                    #很重要，不更新数据写不进去
      row = cursor.next()
    print "Update Success"
  
#Update_Field_Value(r"C:\Users\Hu Fei\Desktop\Data\BloomfieldTownship\SchoolTaxDistrict.shp", r'C:\Users\Hu Fei\Desktop\Data\data1.xls',0, r'FID', r'Other')
