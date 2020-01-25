import csv
with open('names.csv','r',encoding='utf-8') as file:
	reader = csv.reader(file)
	interestingrows=[row for idx, row in enumerate(reader) if idx == 0]
	print(interestingrows)