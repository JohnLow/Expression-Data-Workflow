
#!/usr/bin/python
import csv
import MySQLdb
import rpy


	
db = MySQLdb.Connect(host = "localhost", user= "root", passwd="test", db="test")
cursor = db.cursor()

genelist = []
occurance = []
templist = []

array = list(csv.reader(open(r'test.csv'))) #temp 2d array from csv

#iterates through csv and stores gene names in 1d array
for x in range(1,len(array)):
	for y in range(0,len(array[0])):
		genelist.append(array[x][y]) #genelist is a temporary array




#remove duplicates and whitespace
mylist = list(set(genelist))
mylist.remove("")
 


#searches for gene occurance 
for a in mylist[:]:
	for x in range(1,len(array)):
		for y in range(0,len(array[0])):
			if a == array[x][y]:
				occurance.append([a , array[0][y]])
				

templist = mylist
heoccurance.sort()
mylist.sort()
templist.sort()


for a in mylist[:]:
	
	sql = """INSERT INTO geneoverlaps (geneName, Diseases) Values (""" + "'" + a +"'," + "' '" + ")"
	cursor.execute(sql)
	db.commit()

for b in range(0, len(occurance)):
	
	insert = "UPDATE geneoverlaps SET Diseases = CONCAT (Diseases," + "\"" + occurance[b][1] +", " +"\""  +")" + "WHERE geneName = \"" + occurance[b][0] + "\""

	#"SELECT CONCAT(Diseases," + "\"" + occurance[b][1] +"\""+")" + "FROM geneoverlaps WHERE geneName = \"" + occurance[b][0] + "\"" 
	print insert
	cursor.execute(insert)
	db.commit()
	
