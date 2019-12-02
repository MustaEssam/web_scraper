import csv

oldF = "D:\\work\\compare\\old.csv"
newF = "D:\\work\\compare\\new.csv"

product_name_old = []
sold_old = []
old_price = []
product_name_new = []
sold_new = []
in_stock = []
new_price = []

diff_sold = []
price = []
link = []

file_name = "D:\\work\\compared.csv"
out_file = open(file_name, 'a')
header = "Product Name, new_price -- old_price, Sold in 2 monthes, profit, Link, No. in stock \n"
out_file.write(header)

def read_file(file_name, name, sold, price):
	with open(file_name, 'r') as csv_read: 
		file_csv = csv.reader(csv_read)
		next(file_csv)
		for row in file_csv:
			name.append(row[0])
			price.append(row[1].replace('EGP', '').replace(',', ''))
			sold.append(row[3])


with open(newF, 'r') as csv_read: 
	file_csv = csv.reader(csv_read)
	next(file_csv)
	for row in file_csv:
		in_stock.append(row[5])
		link.append(row[4])

read_file(oldF, product_name_old, sold_old, old_price)
read_file(newF, product_name_new, sold_new, new_price)

#new_set = set(product_name_old) & set(product_name_new)
#print(len(new_set))

i = 0
j = 0
k = 0
for row_new in product_name_new:
	for row_old in product_name_old:
		if row_new == row_old:
			diff_sold.append(int(sold_new[i]) - int(sold_old[j]))
			if float(new_price[i]) == float(old_price[j]):
				price.append(new_price[i])
			else:
				price.append(str(new_price[i]) + '--' + str(old_price[j]))
			out_file.write(row_new + ',' + price[k] + ',' + str(diff_sold[k]) + ',' + str(float(new_price[i]) * diff_sold[k]) + ',' + link[i] + ',' + in_stock[i] + '\n')
			k = k + 1
			j = 0
			break
		else:
			if j > 1447:
				j = 0
				break
			j = j + 1
	i = i + 1


out_file.close()