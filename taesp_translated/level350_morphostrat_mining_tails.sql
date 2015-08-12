-- LAYER NAME level350_morphostrat_mining_tails
SELECT * FROM tp_gu, tblguf WHERE tp_gu.gu_number = tblguf.guno AND tblguf.morphage='h' and tblguf.morph='ht';