#coding=utf-8
import arcpy
import FieldOperation
#import PIL

File_name_path =  "C:\Program Files (x86)\ArcGIS\DeveloperKit10.1\Samples\data\BloomfieldTownship\SchoolTaxDistrict.shp"
Field_name_add = "Other"
Field_type_add="DOUBLE"
Field_name_delete = "TRY"

update_table_path = "C:\Program Files (x86)\ArcGIS\DeveloperKit10.1\Samples\data\BloomfieldTownship\SchoolTaxDistrict.shp" 
input_table_path = 'C:\Users\Administrator\Desktop\data1.csv'
Join_field_name = 'FID'
Add_field_name = 'Other'

FieldOperation.Delete_Field(File_name_path, Field_name_delete)
FieldOperation.Add_Field_Name( File_name_path, Field_name_add, Field_type_add)
FieldOperation.Update_Field_Value(update_table_path, input_table_path, Join_field_name, Add_field_name)

#FieldOperation.AddFieldValue("C:\Program Files (x86)\ArcGIS\DeveloperKit10.1\Samples\data\BloomfieldTownship\SchoolTaxDistrict.shp", "TRY")
#arcpy.ZRenderer_stats(File_name_path, "Other", "C:\Users\Administrator\Desktop\hotspot_output_rendered.lyr")


#mxd = arcpy.mapping.MapDocument(r"C:\Users\Administrator\Desktop\123.mxd")

#arcpy.mapping.ExportToGIF(mxd, r"C:\Users\Administrator\Desktop\1234.gif")
#del mxd

#arcpy.mapping.UpdateLayer()
