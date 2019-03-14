def insert_adv(advanced,year):
	with conn:
		cursor.execute("""INSERT INTO advanced_{}
				VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""".format(str(year)), 
				(advanced.calyear, advanced.Name, advanced.PER,advanced.TSper,advanced.TPAr,
				advanced.FTr,advanced.ORBper,advanced.DRBper,advanced.TRBper,advanced.ASTper,
				advanced.STLper,advanced.BLKper,advanced.TOVper, advanced.USG, advanced.OWS,
				advanced.DWS,advanced.WS,advanced.WS48,advanced.OBPM,advanced.DBPM,
				advanced.BPM,advanced.VORP))

def fill_database_adv(year): #function to make table and fill it with values from a season
	#sheet = wb.sheet_by_name("{}".format(str(year))) #correlates to which year data is being queried
	cursor.execute("""CREATE TABLE if not exists advanced_{}(
		calyear integer, Player text,PER real,TSper real,a3PAr real,FTr real,ORBper real,
		DRBper real,TRBper real, ASTper real,STLper real,BLKper real,TOVper real,USG real,	
		OWS decimal,DWS decimal,WS decimal,WS48 decimal,OBPM decimal,DBPM decimal,
		BPM decimal,VORP decimal)""".format(str(year)))
	i=1	
	while i<=(sheet.nrows-1):
		a = advanced_player(sheet.cell_value(i,0),sheet.cell_value(i,1),sheet.cell_value(i,2),sheet.cell_value(i,3),
		sheet.cell_value(i,4),sheet.cell_value(i,5),sheet.cell_value(i,6),sheet.cell_value(i,7),sheet.cell_value(i,8),
		sheet.cell_value(i,9),sheet.cell_value(i,10),sheet.cell_value(i,11),sheet.cell_value(i,12),sheet.cell_value(i,13),
		sheet.cell_value(i,15),sheet.cell_value(i,16),sheet.cell_value(i,17),sheet.cell_value(i,18),
		sheet.cell_value(i,20),sheet.cell_value(i,21),sheet.cell_value(i,22),sheet.cell_value(i,23))

		insert_adv(a,year)
		i+=1



