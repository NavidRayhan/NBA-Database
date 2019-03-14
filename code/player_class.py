class player:

	def __init__(self, calyear,Name,Pos,Age,G,MP,FG,FGA,FG_perc,m_3P,a_3P, perc_3P, m_2P, a_2P, perc_2P,
				eFG, FT, FTA, perc_FT, ORB, DRB,TRB,AST,STL,BLK,TOV,PF,Points):

		self.calyear = calyear; self.Name = Name;self.Pos = Pos;self.Age = Age;self.G = G
		self.MP = MP; self.FG = FG; self.FGA = FGA; self.FG_perc = FG_perc
		self.m_3P = m_3P; self.a_3P = a_3P; self.perc_3P = perc_3P
		self.m_2P = m_2P; self.a_2P = a_2P; self.perc_2P = perc_2P
		self.eFG =eFG; self.FT = FT; self.FTA= FTA; self.perc_FT = perc_FT
		self.ORB = ORB; self.DRB = DRB; self.TRB =TRB; self.AST= AST
		self.STL = STL; self.BLK = BLK; self.TOV = TOV; self.PF=PF	
		self.Points = Points; 

class advanced:
	def __init__(self,calyear,Name,PER,TS,TPAr,FTr,ORBper,DRBper,TRBper,ASTper,STLper,
		BLKper,TOVper,USG,OWS,DWS,WS,WS48,OBPM,DBPM,BPM,VORP):
	
		self.calyear=calyear;self.Name=Name;self.PER=PER;self.TS=TS;self.TPAr=TPAr;self.FTr=FTr;
		self.ORBper=ORBper;self.DRBper=DRBper;self.TRBper=TRBper;self.ASTper=ASTper;self.STLper=STLper;
		self.BLKper=BLKper;self.TOVper=TOVper;self.USG= USG;self.OWS=OWS;self.DWS= DWS;
		self.WS=WS;self.WS48= WS48;self.OBPM= OBPM;self.DBPM= DBPM;self.BPM= BPM;self.VORP= VORP





