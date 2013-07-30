#coding=utf-8
import arcpy
import FieldOperation
from PIL import Image, ImageSequence
import sys, os
from images2gif import writeGif

def Change_UniqueValuesSymbology( input_file_mxd_path, field_symbol, out_put_gif_path):
     """刷新更新过属性数据的图层.lyr中的UniqueValuesSymbology，并导出静态的GIF"""
     mxd = arcpy.mapping.MapDocument(input_file_mxd_path)
     lyr = arcpy.mapping.ListLayers(mxd)[0]
    
     stateList = []
     rows = arcpy.da.SearchCursor(lyr, [field_symbol])
     for row in rows:
       stateList.append(row[0])
       print "The Field value is: " + str(row[0]) + str( type(row[0]))

     print stateList
     
     if lyr.symbologyType == "UNIQUE_VALUES":
       print "The layer is Unique_Value"
       lyr.symbology.classValues = stateList
       lyr.symbology.showOtherValues = False
     
     arcpy.RefreshActiveView()
     arcpy.RefreshTOC()
     arcpy.mapping.ExportToGIF(mxd, out_put_gif_path)
     del mxd

def Change_GraduatedValuesSymbology( input_file_mxd_path, input_template_lyr_path, field_symbol, out_put_gif_path):
    """刷新更新过属性数据的图层.lyr中的UniqueValuesSymbology，并导出静态的GIF"""
    mxd = arcpy.mapping.MapDocument( input_file_mxd_path )
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    lyr = arcpy.mapping.ListLayers(mxd, "SchoolTaxDistrict", df)[0]
    lyrFile = arcpy.mapping.Layer( input_template_lyr_path)
    arcpy.mapping.UpdateLayer(df, lyr, lyrFile, True)
    if lyr.symbologyType == "GRADUATED_COLORS":
      print r"lyr.symbologyType == GRADUATED_COLORS"
      lyr.symbology.valueField = field_symbol
      lyr.symbology.classBreakValues = [1, 10, 20, 30, 40]
      lyr.symbology.classBreakLabels = ["1 to 30", "30 to 50", 
                                        "5,0 to 70", "70 to 90"]
    arcpy.mapping.ExportToGIF(mxd, out_put_gif_path)
    print 'image success'
  
    del mxd, lyrFile
    
def Make_Animated_Gif( file_names_List, output_AnimatedGif_path ):
    """制作动态Gif"""
    file_names = file_names_List
    #fn = r'C:\Users\Hu Fei\Desktop\Data\10.gifC:\Users\Hu Fei\Desktop\Data\11.gifC:\Users\Hu Fei\Desktop\Data\12.gif'
    #file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.gif')))
    #print file_names
    #['animationframa.png', 'animationframb.png', 'animationframc.png', ...] "
    
    images = [Image.open(fn) for fn in file_names]

    size = (1000,1000)
    for im in images:
        im.thumbnail(size, Image.ANTIALIAS)
    
    #print writeGif.__doc__
    # writeGif(filename, images, duration=0.1, loops=0, dither=1)
    #    Write an animated gif from the specified images.
    #    images should be a list of numpy arrays of PIL images.
    #    Numpy images of type float should have pixels between 0 and 1.
    #    Numpy images of other types are expected to have values between 0 and 255.
    #images.extend(reversed(images)) #infinit loop will go backwards and forwards.
    
    #filename = "C:\Users\Hu Fei\Desktop\Data\my_gif.GIF"
    writeGif(output_AnimatedGif_path, images, duration=0.2)
    print '动态GIF图生成成功'



#Change_UniqueValuesSymbology( r"C:\Users\Hu Fei\Desktop\Data\Test.mxd", r'Other', r"C:\Users\Hu Fei\Desktop\Data\2.gif")
#Change_GraduatedValuesSymbology( r"C:\Users\Hu Fei\Desktop\Data\Test.mxd", r"C:\Users\Hu Fei\Desktop\Data\Template.lyr", r'Other', r"C:\Users\Hu Fei\Desktop\Data\3.gif")
#Make_Animated_Gif( [r'C:\Users\Hu Fei\Desktop\Data\10.gif',r'C:\Users\Hu Fei\Desktop\Data\11.gif',r'C:\Users\Hu Fei\Desktop\Data\12.gif'],"C:\Users\Hu Fei\Desktop\Data\my_gif.GIF")
