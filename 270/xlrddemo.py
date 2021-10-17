import xlrd, json

data = xlrd.open_workbook("F:/文档/工作文档/少儿编程/闫澳帆与陈一铭/文件的操作/Book1.xlsx")
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    print(table.row_values(i))


