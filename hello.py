#coding=utf-8
import arcpy
import FieldOperation
import ExportMap
#import PIL

File_name_path =  r"C:\Users\Hu Fei\Desktop\Data\BloomfieldTownship\SchoolTaxDistrict.shp"
Field_name_add = r"Other"
Field_type_add= r"DOUBLE"
Field_name_delete = r"TRY"

update_table_path = r"C:\Users\Hu Fei\Desktop\Data\\BloomfieldTownship\SchoolTaxDistrict.shp" 
input_table_path = [r'C:\Users\Hu Fei\Desktop\Data\data1.csv',r'C:\Users\Hu Fei\Desktop\Data\data2.csv',r'C:\Users\Hu Fei\Desktop\Data\data3.csv']
Join_field_name = r'FID'
Add_field_name = r'Other'

#FieldOperation.Delete_Field(File_name_path, Field_name_delete)
#FieldOperation.Add_Field_Name( File_name_path, Field_name_add, Field_type_add)
#FieldOperation.Update_Field_Value(update_table_path, input_table_path, Join_field_name, Add_field_name)
csv = ''

i = 10
for csv in input_table_path:
	FieldOperation.Update_Field_Value(update_table_path, csv, Join_field_name, Add_field_name)
	out_put = r'C:\Users\Hu Fei\Desktop\Data' + '\\' + str(i) + '.gif'
	ExportMap.Change_GraduatedValuesSymbology( r"C:\Users\Hu Fei\Desktop\Data\Test.mxd", r"C:\Users\Hu Fei\Desktop\Data\Temp.lyr", r'Other', out_put)
	i = i + 1

#FieldOperation.AddFieldValue("C:\Program Files (x86)\ArcGIS\DeveloperKit10.1\Samples\data\BloomfieldTownship\SchoolTaxDistrict.shp", "TRY")
#arcpy.ZRenderer_stats(File_name_path, "Other", "C:\Users\Administrator\Desktop\hotspot_output_rendered.lyr")

#ExportMap.Change_GraduatedValuesSymbology( r"C:\Users\Hu Fei\Desktop\Data\Test.mxd", r"C:\Users\Hu Fei\Desktop\Data\Template.lyr", r'Other', r"C:\Users\Hu Fei\Desktop\Data\3.gif")
