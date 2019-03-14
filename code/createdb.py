'''
Functions to create and update large dataset of all NBA Basic stats for every player from 2000-2018:
'''
import sqlite3
from player_class import *
import xlrd

loc = "C:\\Users\\Navid\\Documents\\Data Science\\NBA databases\\basic_stats_2010s.xlsx"
wb = xlrd.open_workbook(loc)
conn = sqlite3.connect("Regular_szn_basic_advanced.db")
cursor = conn.cursor()
conn.commit()

#function to create a table listing one player's stats
def insert(play,year):
	with conn:
		cursor.execute("""INSERT INTO player_{}
				VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""".format(str(year)), (play.calyear, play.Name, 
					play.Pos, play.Age, play.G, play.MP, play.FG,play.FGA,play.FG_perc,
					play.m_3P,play.a_3P, play.perc_3P, play.m_2P, play.a_2P,play.perc_2P,
					play.eFG, play.FT, play.FTA, play.perc_FT, play.ORB, play.DRB,play.TRB,
					play.AST,play.STL,play.BLK,play.TOV,play.PF,play.Points))

#function to make table and fill it with stats of all players from a season
def fill_database(year): 
	sheet = wb.sheet_by_name("{}".format(str(year))) #correlates to which year data is being queried
	cursor.execute("""CREATE TABLE if not exists player_{}(
		calyear integer, Player text, Pos text, Age integer, G integer, MP real, FG real, FGA real, FG_perc real,	
		m_3P real, a_3P real, perc_3P real, m_2P real, a_2P real, perc_2P real,	eFG real,	
		FT real, FTA real, perc_FT real, ORB real, DRB real, TRB real, AST real, STL real,	
		BLK	real, TOV real,	PF real, Points real	
		)""".format(str(year)))
	i=1	
	while i<=(sheet.nrows-1):#covering all of the excel sheets in the file
		a = player(sheet.cell_value(i,0),sheet.cell_value(i,1),sheet.cell_value(i,2),sheet.cell_value(i,3),sheet.cell_value(i,4),sheet.cell_value(i,5),
		sheet.cell_value(i,6),sheet.cell_value(i,7),sheet.cell_value(i,8),sheet.cell_value(i,9),sheet.cell_value(i,10),
		sheet.cell_value(i,11),sheet.cell_value(i,12),sheet.cell_value(i,13),sheet.cell_value(i,14),sheet.cell_value(i,15),
		sheet.cell_value(i,16),sheet.cell_value(i,17),sheet.cell_value(i,18),sheet.cell_value(i,19),sheet.cell_value(i,20),
		sheet.cell_value(i,21),sheet.cell_value(i,22),sheet.cell_value(i,23),sheet.cell_value(i,24),sheet.cell_value(i,25),
		sheet.cell_value(i,26),sheet.cell_value(i,27))

		insert(a,year)
		i+=1

#used to create or overwrite a dataset that combines 2 or more datasets (NBA seasons)
def table_creator(yr):
	cursor.execute("DROP TABLE if exists all_basic_stats"); conn.commit()
	cursor.execute("DROP TABLE if exists temp")
	cursor.execute("""CREATE table if not exists all_basic_stats as SELECT * from player_{}
	""".format(str(yr))); conn.commit()
	
	while yr > 2000:
		yr-=1
		cursor.execute("""CREATE table temp as SELECT * from all_basic_stats
			UNION SELECT * from player_{} """.format(str(yr)))
		conn.commit()
		cursor.execute("DROP TABLE all_basic_stats"); conn.commit()
		cursor.execute("CREATE TABLE  all_basic_stats as SELECT * from temp"); conn.commit()
		cursor.execute("drop table temp")

#makes tables of all years basic stats from yr to 2019 
def make_database(yr):
	while yr < 2020:
		cursor.execute("DROP TABLE if exists player_{}".format(str(yr)))
		fill_database(yr)
		yr+=1

#run this to create large dataset of all NBA Basic stats for every player from 2000-2019:

fill_database(2019)
make_database(2000)
table_creator(2019)	

