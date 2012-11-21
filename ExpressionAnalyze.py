#!/usr/bin/python
import csv
from rpy import *


#loading = list(csv.reader(open(r'expression.csv')))
loading = list(csv.reader(open(r'expression.csv'), delimiter=',', quotechar='\''))

#gathers ID and ID index
col1 = []
for x in range(1, len(loading)):
	col1.append(loading[x][0])



#get end range of healthy 

#ranges will be hardcoded for now
healthyEnd = 6

healthy_data = []

#get healthy data in a 2d array
csvLen = len(loading)
for line in xrange(csvLen):
	healthy_data.append([])
	for Hcol in range(1,healthyEnd+1):
		if line != 0:
			
			healthy_data[line].append(loading[line][Hcol])



#convert data to float
healthy_values = []

for line1 in xrange(len(healthy_data)):
	healthy_values.append([])
	for Hcol2 in range(0,healthyEnd):
		if line1 != 0:
			hey = float(healthy_data[line1][Hcol2])
			healthy_values[line1].append(hey)



#get disease data in a 2d array
disease_data = []
csvLen = len(loading)
for line in xrange(csvLen):
	disease_data.append([])
	for Hcol in range(healthyEnd+2, len(loading[1])):
		if line != 0:
			disease_data[line].append(loading[line][Hcol])



#convert data to float
disease_values = []

for line1 in xrange(len(disease_data)):
	disease_values.append([])
	for Hcol2 in range(0,len(disease_data[1])):
		if line1 != 0:
			hey = float(disease_data[line1][Hcol2])
			disease_values[line1].append(hey)

raw_p = []
adj_p = []
for t_range in range(1,len(loading)):
	a = healthy_values[t_range]
	b = disease_values[t_range]

	raw_p.append(r.t_test(a,b)['p.value'])


adj_p.append(r.p_adjust(raw_p, "BH", n= len(raw_p)))

print col1
print raw_p
print adj_p