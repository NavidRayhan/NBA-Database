'''
Functions to create and update large dataset of all NBA Advanced stats for every player from 2000-2018:
'''
import sqlite3
from player_class import *
import xlrd

loc = "C:\\Users\\Navid\\Documents\\Data Science\\NBA databases\\advanced_stats_2010s.xlsx"
wb = xlrd.open_workbook(loc)
conn = sqlite3.connect("Regular_szn_basic_advanced.db")
cursor = conn.cursor()
conn.commit()

#function to create a table listing one player's advanced stats
def insert_adv(advanced,year):
	with conn:
		cursor.execute("""INSERT INTO advanced_{}
				VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""".format(str(year)), 
				(advanced.calyear, advanced.Name, advanced.PER,advanced.TS,advanced.TPAr,
				advanced.FTr,advanced.ORBper,advanced.DRBper,advanced.TRBper,advanced.ASTper,
				advanced.STLper,advanced.BLKper,advanced.TOVper, advanced.USG,advanced.OWS,
				advanced.DWS,advanced.WS,advanced.WS48,advanced.OBPM, advanced.DBPM, advanced.BPM,advanced.VORP))

#function to make table and fill it with advanced stats of all players from a season
def fill_database_adv(year):
	sheet = wb.sheet_by_name("{}".format(str(year))) #correlates to which year data is being queried
	cursor.execute("""CREATE TABLE if not exists advanced_{}(
		calyear integer, Player text,PER real,TS real,TPAr real,FTr real,ORBper real,
		DRBper real,TRBper real, ASTper real,STLper real,BLKper real,TOVper real,USG real,	
		OWS decimal,DWS decimal,WS decimal,WS48 decimal,OBPM decimal,DBPM decimal,
		BPM decimal,VORP decimal)""".format(str(year)))
	i=1	
	while i<=(sheet.nrows-1):
		a = advanced(sheet.cell_value(i,0),sheet.cell_value(i,1),sheet.cell_value(i,2),sheet.cell_value(i,3),sheet.cell_value(i,4),sheet.cell_value(i,5),
		sheet.cell_value(i,6),sheet.cell_value(i,7),sheet.cell_value(i,8),sheet.cell_value(i,9),sheet.cell_value(i,10),
		sheet.cell_value(i,11),sheet.cell_value(i,12),sheet.cell_value(i,13),sheet.cell_value(i,14),sheet.cell_value(i,15),
		sheet.cell_value(i,16),sheet.cell_value(i,17),sheet.cell_value(i,18),sheet.cell_value(i,19),sheet.cell_value(i,20),
		sheet.cell_value(i,21))

		insert_adv(a,year)
		i+=1

#used to create or overwrite a dataset that combines 2 or more datasets (NBA seasons)
def table_creator_adv(yr):
	cursor.execute("DROP TABLE if exists all_advanced_stats"); conn.commit()
	cursor.execute("DROP TABLE if exists temp1")
	cursor.execute("""CREATE table all_advanced_stats as SELECT * from advanced_{}
	""".format(str(yr))); conn.commit()
	
	while yr > 2000:
		yr-=1
		cursor.execute("""CREATE table temp1 as SELECT * from all_advanced_stats
			UNION SELECT * from advanced_{} """.format(str(yr)))
		conn.commit()
		cursor.execute("DROP TABLE all_advanced_stats"); conn.commit()
		cursor.execute("CREATE TABLE  all_advanced_stats as SELECT * from temp1"); conn.commit()
		cursor.execute("drop table temp1")

#makes tables of all years basic stats from yr to 2019
def make_database_adv(yr):
	while yr < 2020:
		cursor.execute("DROP TABLE if exists advanced_{}".format(str(yr)))
		fill_database_adv(yr)
		yr+=1


#run this to create large dataset of all NBA Basic stats for every player from 2000-2019:

fill_database_adv(2019)
make_database_adv(2000)
table_creator_adv(2019)	
