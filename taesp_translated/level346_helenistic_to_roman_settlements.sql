-- LAYER NAME level346_helenistic_to_roman_settlements
SELECT * FROM tp_posi, tblposirec WHERE tp_posi.posi_no = tblposirec.posino AND tblposirec.settchk=1 and tblposirec.hrchk=1