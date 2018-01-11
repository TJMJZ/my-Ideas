

bridgePiers:
# for payment:
# establish piertable{bridgeName,pierId,stageID,startHeight,height,{payments}}

# NOT YET
# establish amounttable{bridgeName,}




tunnel:

rockcatagorytable:rockcatagory,number,length:using excel and vba

input:topheading,bench,invert,...

get tunnel (payed) sections
with portal,paymentID,length get():mile1,mile2

# no need at all
with mile1,mile2 get category1,2
draw by cell,conditional formatting by category_average

or draw all

---------
T-T-B-P
O-O-E-A
T-P-N-Y
A- -C
L- -H


# for viewing
for each bridgeLR:
	get pierDict
	generate empty pierTable
	column = 0

	for each pier in pierDict:
		row = 0
		piertable[row][column] = pierName
		piertable[row][column+1] = spanName

		for each stage in pier:
			# build stage list
			stageList.append(stage)

		while true:
			findmax in stageList
			eliminate max
			row += 1

			pierTable[row][column] = stageHeight



			if pier is payed:
				change piercell color
			elif: pier is done: # need curr progress and judgefunction

		column += 2

