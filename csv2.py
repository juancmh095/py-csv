import csv
import re
import time
import datetime

with open('528118808620.csv', newline='') as File:
	dataRes = []
	dateRes = 0
	reader = csv.reader(File)
	
	for row in reader:
		try:
			date = row[1]

			date2 = date.split(' ')

			if(date != ''):
				fecha = date2[0]
				hora = date2[1]
				cord = row[9]

				row[1] = fecha
				row[2] = hora

				regex = r"[\/,\[,\]]"
				test_str = cord
				subst = " "
				result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

				cord2 = result.split(' ')
				if(len(cord2) > 3):
					lat = cord2[1]
					longg = cord2[2]

					row[7] = lat
					row[8] = longg

			
			""" lat = row[8]
			latRes = 0
			lonRes = 0

			regex1 = r"[°,',N,\"]"
			subst1 = "-"
			result1 = re.sub(regex1, subst1, lat, 0, re.MULTILINE)
			latR1 = result1.split('-')
			if len(latR1)>1:
				latRes = int(latR1[0])+(int(latR1[1])/60)+(int(latR1[2])/3600)
			
			lon = row[9]
			regex2 = r"[°,',N,\"]"
			subst2 = "-"
			result2 = re.sub(regex2, subst2, lon, 0, re.MULTILINE)
			lonR1 = result2.split('-')
			if len(lonR1) > 1:
				lonRes = (int(lonR1[0])+(int(lonR1[1])/60)+(int(lonR1[2])/3600))*(-1)
			


			s = row[4] + row[5]
			dateRes = time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y%H:%M:%S").timetuple()) """
			
		except:
			pass
		finally:
			""" row.append(latRes)
			row.append(lonRes)
			row.append(dateRes)
			
			print(row)
			print(dateRes, s) """
			if(row[1] != ''):
				if(row[7] != '' and row[8] != ''):
					dataRes.append(row)
	
	myFile = open('new2.csv', 'w')
	with myFile:
		print(len(dataRes))
		writer = csv.writer(myFile)
		writer.writerows(dataRes)
	print("Writing complete")



