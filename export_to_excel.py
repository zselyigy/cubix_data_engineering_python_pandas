def dataframe_export_to_new_excel(df_export, basepath, outputfolder, xlsx_name, outputsheet):
      df_export.to_excel(basepath + '\\' + outputfolder + '\\' + xlsx_name,
          index = False, sheet_name= outputsheet)
      print('Exported to new Excel file!')

def dataframe_export_to_existing_excel(df_export, basepath, outputfolder, xlsx_name, outputsheet):
      import openpyxl, pandas as pd
      with pd.ExcelWriter(basepath + '\\' + outputfolder + '\\' + xlsx_name,
                    engine= 'openpyxl', mode= 'a') as writer:
            df_export.to_excel(writer, index = False, sheet_name= outputsheet)
            print('Exported to an existing Excel file!')