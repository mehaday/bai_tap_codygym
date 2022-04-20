import pandas as pd

df = pd.read_csv('git\pandas_1\OnlineRetail.csv',encoding='unicode_escape')
df.info() #kiểu dữ liệu của các thuộc tính
df.shape #số dòng, số cột
#Trích xuất dữ liệu các cột Description và Quantity lưu vào file OnlineRetail.csv
df.loc[:,['Description','Quantity']].to_csv('Onlineretail.csv')

#Trích xuất dữ liệu 1000 dòng đầu tiên lưu vào file OnlineRetail.xlsx
df.loc[:999].to_excel('Onlineretail.xlsx')

#Trích xuất các bản ghi có số lượng từ 10 trở lên lưu vào file OnlineRetail.h5
df.loc[df.Quantity > 10].to_hdf('Onlineretail.h5',key='df')

#Trích xuất dữ liệu các phần tử từ dòng 1000 đến dòng 2000, các cột Quantity, InvoiceDate, UnitPrice lưu vào file OnlineRetail.json
df.loc[999:1999,['InvoiceDate','Quantity','UnitPrice']].to_json('Onlineretail.json')

#Trích xuất các bản ghi có số hóa đơn ‘536365’ lưu vào file OnlineRetail.html
df.loc[:,df.InvoiceNo == 536365].to_html('Onlineretail.html')







