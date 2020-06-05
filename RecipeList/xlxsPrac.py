import xlsxwriter, os, time

# Creating Work book and adding Worksheets
while 1:
    workbook = xlsxwriter.Workbook('Recipe.xlsx')
    worksheet = workbook.add_worksheet()

    merge_format = workbook.add_format({
    'bold': True,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#D7E4BC',
    'size': 16,
    'font_name': 'Source Sans Pro',
    })

    worksheet.write(5, 7, 'ss3ss')
    worksheet.merge_range(1,0,1,6,'Write',merge_format)


    try:
        workbook.close()
    except PermissionError:
        os.system("TASKKILL /F /IM excel.exe")
        time.sleep(2)
        os.remove("Recipe.xlsx")
        continue
    break

os.system("start " + 'Recipe.xlsx')
