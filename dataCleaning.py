import pandas as pd
import chardet

def main():
	file = "Speed Dating Data.csv"
	#file = "Workbook1.csv"
	with open('Speed Dating Data.csv', 'rb') as f:
	#with open('Workbook1.csv', 'rb') as f:
		result = chardet.detect(f.read())  # or readline if the file is large
	dataFrame = pd.read_csv('Speed Dating Data.csv', encoding=result['encoding'])
	#dataFrame = pd.read_csv('Workbook1.csv', encoding=result['encoding'])
	
	dataFrame = dataFrame.drop("iid", 1)
	dataFrame = dataFrame.drop("id", 1)
	dataFrame = dataFrame.drop("idg", 1)
	dataFrame = dataFrame.drop("pid", 1)
	
	dataFrame = dataFrame.drop("from", 1)
	
	dataFrame = dataFrame.drop("undergra", 1)
	dataFrame = dataFrame.drop("mn_sat", 1)
	dataFrame = dataFrame.drop("tuition", 1)
	
	#dataFrame = dataFrame.drop("length", 1)
	
	dataFrame = dataFrame.drop("met", 1)
	dataFrame = dataFrame.drop("dec", 1)
	dataFrame = dataFrame.drop("like", 1)
	dataFrame = dataFrame.drop("expnum", 1)
	dataFrame = dataFrame.drop("income", 1)
	dataFrame = dataFrame.drop("int_corr", 1)
	
	dataFrame = dataFrame.drop("attr2_1", 1)
	dataFrame = dataFrame.drop("sinc2_1", 1)
	dataFrame = dataFrame.drop("intel2_1", 1)
	dataFrame = dataFrame.drop("amb2_1", 1)
	dataFrame = dataFrame.drop("shar2_1", 1)
	dataFrame = dataFrame.drop("fun2_1", 1)
	
	dataFrame = dataFrame.drop("attr4_1", 1)
	dataFrame = dataFrame.drop("sinc4_1", 1)
	dataFrame = dataFrame.drop("intel4_1", 1)
	dataFrame = dataFrame.drop("amb4_1", 1)
	dataFrame = dataFrame.drop("shar4_1", 1)
	dataFrame = dataFrame.drop("fun4_1", 1)
	
	dataFrame = dataFrame.drop("attr5_1", 1)
	dataFrame = dataFrame.drop("sinc5_1", 1)
	dataFrame = dataFrame.drop("intel5_1", 1)
	dataFrame = dataFrame.drop("amb5_1", 1)
	dataFrame = dataFrame.drop("fun5_1", 1)
	
	dataFrame = dataFrame.drop("satis_2", 1)
	dataFrame = dataFrame.drop("numdat_2", 1)
	
	dataFrame = dataFrame.drop("attr1_2", 1)
	dataFrame = dataFrame.drop("sinc1_2", 1)
	dataFrame = dataFrame.drop("intel1_2", 1)
	dataFrame = dataFrame.drop("amb1_2", 1)
	dataFrame = dataFrame.drop("shar1_2", 1)
	dataFrame = dataFrame.drop("fun1_2", 1)
	
	dataFrame = dataFrame.drop("attr7_2", 1)
	dataFrame = dataFrame.drop("sinc7_2", 1)
	dataFrame = dataFrame.drop("intel7_2", 1)
	dataFrame = dataFrame.drop("amb7_2", 1)
	dataFrame = dataFrame.drop("shar7_2", 1)
	dataFrame = dataFrame.drop("fun7_2", 1)
	
	dataFrame = dataFrame.drop("attr4_2", 1)
	dataFrame = dataFrame.drop("sinc4_2", 1)
	dataFrame = dataFrame.drop("intel4_2", 1)
	dataFrame = dataFrame.drop("amb4_2", 1)
	dataFrame = dataFrame.drop("shar4_2", 1)
	dataFrame = dataFrame.drop("fun4_2", 1)
	
	dataFrame = dataFrame.drop("attr2_2", 1)
	dataFrame = dataFrame.drop("sinc2_2", 1)
	dataFrame = dataFrame.drop("intel2_2", 1)
	dataFrame = dataFrame.drop("amb2_2", 1)
	dataFrame = dataFrame.drop("shar2_2", 1)
	dataFrame = dataFrame.drop("fun2_2", 1)
	
	dataFrame = dataFrame.drop("attr3_2", 1)
	dataFrame = dataFrame.drop("sinc3_2", 1)
	dataFrame = dataFrame.drop("intel3_2", 1)
	dataFrame = dataFrame.drop("amb3_2", 1)
	dataFrame = dataFrame.drop("fun3_2", 1)
	
	dataFrame = dataFrame.drop("attr5_2", 1)
	dataFrame = dataFrame.drop("sinc5_2", 1)
	dataFrame = dataFrame.drop("intel5_2", 1)
	dataFrame = dataFrame.drop("amb5_2", 1)
	dataFrame = dataFrame.drop("fun5_2", 1)
	
	dataFrame = dataFrame.drop("numdat_3", 1)
	
	dataFrame = dataFrame.drop("match_es", 1)
	dataFrame = dataFrame.drop("you_call", 1)
	dataFrame = dataFrame.drop("them_cal", 1)
	
	dataFrame = dataFrame.drop("date_3", 1)

	dataFrame = dataFrame.drop("num_in_3", 1)
	
	dataFrame = dataFrame.drop("attr1_3", 1)
	dataFrame = dataFrame.drop("sinc1_3", 1)
	dataFrame = dataFrame.drop("intel1_3", 1)
	dataFrame = dataFrame.drop("amb1_3", 1)
	dataFrame = dataFrame.drop("shar1_3", 1)
	dataFrame = dataFrame.drop("fun1_3", 1)
	
	dataFrame = dataFrame.drop("attr7_3", 1)
	dataFrame = dataFrame.drop("sinc7_3", 1)
	dataFrame = dataFrame.drop("intel7_3", 1)
	dataFrame = dataFrame.drop("amb7_3", 1)
	dataFrame = dataFrame.drop("shar7_3", 1)
	dataFrame = dataFrame.drop("fun7_3", 1)
	
	dataFrame = dataFrame.drop("attr4_3", 1)
	dataFrame = dataFrame.drop("sinc4_3", 1)
	dataFrame = dataFrame.drop("intel4_3", 1)
	dataFrame = dataFrame.drop("amb4_3", 1)
	dataFrame = dataFrame.drop("shar4_3", 1)
	dataFrame = dataFrame.drop("fun4_3", 1)
	
	dataFrame = dataFrame.drop("attr2_3", 1)
	dataFrame = dataFrame.drop("sinc2_3", 1)
	dataFrame = dataFrame.drop("intel2_3", 1)
	dataFrame = dataFrame.drop("amb2_3", 1)
	dataFrame = dataFrame.drop("shar2_3", 1)
	dataFrame = dataFrame.drop("fun2_3", 1)
	
	dataFrame = dataFrame.drop("attr3_3", 1)
	dataFrame = dataFrame.drop("sinc3_3", 1)
	dataFrame = dataFrame.drop("intel3_3", 1)
	dataFrame = dataFrame.drop("amb3_3", 1)
	dataFrame = dataFrame.drop("fun3_3", 1)
	
	dataFrame = dataFrame.drop("attr5_3", 1)
	dataFrame = dataFrame.drop("sinc5_3", 1)
	dataFrame = dataFrame.drop("intel5_3", 1)
	dataFrame = dataFrame.drop("amb5_3", 1)
	dataFrame = dataFrame.drop("fun5_3", 1)
	
	dataFrame['gender'].fillna(1, inplace=True)
	dataFrame['condtn'].fillna(2, inplace=True)
	dataFrame['wave'].fillna(21, inplace=True)
	dataFrame['round'].fillna(18, inplace=True)
	dataFrame['position'].fillna(3, inplace=True)
	dataFrame['positin1'].fillna(5, inplace=True)
	dataFrame['order'].fillna(4, inplace=True)
	dataFrame['partner'].fillna(1, inplace=True)
	dataFrame['match'].fillna(0, inplace=True)
	dataFrame['samerace'].fillna(0, inplace=True)
	dataFrame['age_o'].fillna(27, inplace=True)
	dataFrame['race_o'].fillna(2, inplace=True)
	dataFrame['pf_o_att'].fillna(20, inplace=True)
	dataFrame['pf_o_sin'].fillna(20, inplace=True)
	dataFrame['pf_o_int'].fillna(20, inplace=True)
	dataFrame['pf_o_fun'].fillna(20, inplace=True)
	dataFrame['pf_o_amb'].fillna(10, inplace=True)
	dataFrame['pf_o_sha'].fillna(10, inplace=True)
	dataFrame['dec_o'].fillna(0, inplace=True)
	dataFrame['attr_o'].fillna(6, inplace=True)
	dataFrame['sinc_o'].fillna(8, inplace=True)
	dataFrame['intel_o'].fillna(8, inplace=True)
	dataFrame['fun_o'].fillna(7, inplace=True)
	dataFrame['amb_o'].fillna(7, inplace=True)
	dataFrame['shar_o'].fillna(5, inplace=True)
	dataFrame['like_o'].fillna(7, inplace=True)
	dataFrame['prob_o'].fillna(5, inplace=True)
	dataFrame['met_o'].fillna(2, inplace=True)
	dataFrame['age'].fillna(27, inplace=True)
	dataFrame['field']= dataFrame['field'].str.upper()
	dataFrame["field"].fillna("LAW", inplace = True)
	dataFrame['field_cd'].fillna(8, inplace=True)
	dataFrame['race'].fillna(2, inplace=True)
	dataFrame['imprace'].fillna(1, inplace=True)
	dataFrame['imprelig'].fillna(1, inplace=True)
	dataFrame['zipcode'].fillna(60611, inplace=True)
	dataFrame['goal'].fillna(1, inplace=True)
	dataFrame['date'].fillna(6, inplace=True)
	dataFrame['go_out'].fillna(2, inplace=True)
	dataFrame["career"] = dataFrame['career'].str.upper()
	dataFrame["career"].fillna("LAWER", inplace = True)
	dataFrame['career_c'].fillna(2, inplace=True)
	dataFrame['sports'].fillna(8, inplace=True)
	dataFrame['tvsports'].fillna(1, inplace=True)
	dataFrame['exercise'].fillna(8, inplace=True)
	dataFrame['dining'].fillna(8, inplace=True)
	dataFrame['museums'].fillna(7, inplace=True)
	dataFrame['art'].fillna(8, inplace=True)
	dataFrame['hiking'].fillna(8, inplace=True)
	dataFrame['gaming'].fillna(1, inplace=True)
	dataFrame['clubbing'].fillna(8, inplace=True)
	dataFrame['reading'].fillna(9, inplace=True)
	dataFrame['tv'].fillna(6, inplace=True)
	dataFrame['theater'].fillna(7, inplace=True)
	dataFrame['movies'].fillna(8, inplace=True)
	dataFrame['concerts'].fillna(7, inplace=True)
	dataFrame['music'].fillna(10, inplace=True)
	dataFrame['shopping'].fillna(7, inplace=True)
	dataFrame['yoga'].fillna(1, inplace=True)
	dataFrame['exphappy'].fillna(5, inplace=True)
	dataFrame['attr1_1'].fillna(20, inplace=True)
	dataFrame['sinc1_1'].fillna(20, inplace=True)
	dataFrame['intel1_1'].fillna(20, inplace=True)
	dataFrame['fun1_1'].fillna(20, inplace=True)
	dataFrame['amb1_1'].fillna(10, inplace=True)
	dataFrame['shar1_1'].fillna(10, inplace=True)
	dataFrame['attr3_1'].fillna(7, inplace=True)
	dataFrame['sinc3_1'].fillna(9, inplace=True)
	dataFrame['fun3_1'].fillna(8, inplace=True)
	dataFrame['intel3_1'].fillna(8, inplace=True)
	dataFrame['amb3_1'].fillna(8, inplace=True)
	dataFrame['attr'].fillna(6, inplace = True)
	dataFrame['sinc'].fillna(8, inplace=True)
	dataFrame['intel'].fillna(8, inplace=True)
	dataFrame['fun'].fillna(7, inplace=True)
	dataFrame['amb'].fillna(7, inplace=True)
	dataFrame['shar'].fillna(5, inplace=True)
	dataFrame['prob'].fillna(5, inplace=True)
	dataFrame['attr1_s'].fillna(20, inplace=True)
	dataFrame['sinc1_s'].fillna(10, inplace=True)
	dataFrame['intel1_s'].fillna(20, inplace=True)
	dataFrame['fun1_s'].fillna(20, inplace=True)
	dataFrame['amb1_s'].fillna(10, inplace=True)
	dataFrame['shar1_s'].fillna(10, inplace=True)
	dataFrame['attr3_s'].fillna(7, inplace=True)
	dataFrame['sinc3_s'].fillna(8, inplace=True)
	dataFrame['intel3_s'].fillna(8, inplace=True)
	dataFrame['fun3_s'].fillna(8, inplace=True)
	dataFrame['amb3_s'].fillna(9, inplace=True)
	dataFrame['length'].fillna(1, inplace=True)
	
	dataFrame.insert(10,'pf_o_att_x',int)
	dataFrame.insert(10,'pf_o_sin_x',int)
	dataFrame.insert(10,'pf_o_int_x',int)
	dataFrame.insert(10,'pf_o_fun_x',int)
	dataFrame.insert(10,'pf_o_amb_x',int)
	dataFrame.insert(10,'pf_o_sha_x',int)
	
	dataFrame['pf_o_att_x'] = dataFrame['pf_o_att']/(dataFrame['pf_o_sin']+dataFrame['pf_o_att']+dataFrame['pf_o_int']+dataFrame['pf_o_fun']+dataFrame['pf_o_amb']+dataFrame['pf_o_sha'])
	dataFrame['pf_o_sin_x'] = dataFrame['pf_o_sin']/(dataFrame['pf_o_sin']+dataFrame['pf_o_att']+dataFrame['pf_o_int']+dataFrame['pf_o_fun']+dataFrame['pf_o_amb']+dataFrame['pf_o_sha'])
	dataFrame['pf_o_int_x'] = dataFrame['pf_o_int']/(dataFrame['pf_o_sin']+dataFrame['pf_o_att']+dataFrame['pf_o_int']+dataFrame['pf_o_fun']+dataFrame['pf_o_amb']+dataFrame['pf_o_sha'])
	dataFrame['pf_o_fun_x'] = dataFrame['pf_o_fun']/(dataFrame['pf_o_sin']+dataFrame['pf_o_att']+dataFrame['pf_o_int']+dataFrame['pf_o_fun']+dataFrame['pf_o_amb']+dataFrame['pf_o_sha'])
	dataFrame['pf_o_amb_x'] = dataFrame['pf_o_amb']/(dataFrame['pf_o_sin']+dataFrame['pf_o_att']+dataFrame['pf_o_int']+dataFrame['pf_o_fun']+dataFrame['pf_o_amb']+dataFrame['pf_o_sha'])
	dataFrame['pf_o_sha_x'] = dataFrame['pf_o_sha']/(dataFrame['pf_o_sin']+dataFrame['pf_o_att']+dataFrame['pf_o_int']+dataFrame['pf_o_fun']+dataFrame['pf_o_amb']+dataFrame['pf_o_sha'])
	
	dataFrame['pf_o_att_x'] = dataFrame['pf_o_att_x']*100
	dataFrame['pf_o_sin_x'] = dataFrame['pf_o_sin_x']*100
	dataFrame['pf_o_int_x'] = dataFrame['pf_o_int_x']*100
	dataFrame['pf_o_fun_x'] = dataFrame['pf_o_fun_x']*100
	dataFrame['pf_o_amb_x'] = dataFrame['pf_o_amb_x']*100
	dataFrame['pf_o_sha_x'] = dataFrame['pf_o_sha_x']*100
	
	dataFrame.insert(10,'attr1_s_x',int)
	dataFrame.insert(10,'sinc1_s_x',int)
	dataFrame.insert(10,'intel1_s_x',int)
	dataFrame.insert(10,'fun1_s_x',int)
	dataFrame.insert(10,'amb1_s_x',int)
	dataFrame.insert(10,'shar1_s_x',int)
	
	dataFrame['attr1_s_x'] = dataFrame['attr1_s']/(dataFrame['attr1_s']+dataFrame['sinc1_s']+dataFrame['intel1_s']+dataFrame['fun1_s']+dataFrame['amb1_s']+dataFrame['shar1_s'])
	dataFrame['sinc1_s_x'] = dataFrame['sinc1_s']/(dataFrame['attr1_s']+dataFrame['sinc1_s']+dataFrame['intel1_s']+dataFrame['fun1_s']+dataFrame['amb1_s']+dataFrame['shar1_s'])
	dataFrame['intel1_s_x'] = dataFrame['intel1_s']/(dataFrame['attr1_s']+dataFrame['sinc1_s']+dataFrame['intel1_s']+dataFrame['fun1_s']+dataFrame['amb1_s']+dataFrame['shar1_s'])
	dataFrame['fun1_s_x'] = dataFrame['fun1_s']/(dataFrame['attr1_s']+dataFrame['sinc1_s']+dataFrame['intel1_s']+dataFrame['fun1_s']+dataFrame['amb1_s']+dataFrame['shar1_s'])
	dataFrame['amb1_s_x'] = dataFrame['amb1_s']/(dataFrame['attr1_s']+dataFrame['sinc1_s']+dataFrame['intel1_s']+dataFrame['fun1_s']+dataFrame['amb1_s']+dataFrame['shar1_s'])
	dataFrame['shar1_s_x'] = dataFrame['shar1_s']/(dataFrame['attr1_s']+dataFrame['sinc1_s']+dataFrame['intel1_s']+dataFrame['fun1_s']+dataFrame['amb1_s']+dataFrame['shar1_s'])
	
	dataFrame['attr1_s_x'] = dataFrame['attr1_s_x']*100
	dataFrame['sinc1_s_x'] = dataFrame['sinc1_s_x']*100
	dataFrame['intel1_s_x'] = dataFrame['intel1_s_x']*100
	dataFrame['fun1_s_x'] = dataFrame['fun1_s_x']*100
	dataFrame['amb1_s_x'] = dataFrame['amb1_s_x']*100
	dataFrame['shar1_s_x'] = dataFrame['shar1_s_x']*100
	
	dataFrame.insert(10,'attr3_s_x',int)
	dataFrame.insert(10,'sinc3_s_x',int)
	dataFrame.insert(10,'intel3_s_x',int)
	dataFrame.insert(10,'fun3_s_x',int)
	dataFrame.insert(10,'amb3_s_x',int)
	
	dataFrame['attr3_s_x'] = dataFrame['attr3_s']/(dataFrame['attr3_s']+dataFrame['sinc3_s']+dataFrame['intel3_s']+dataFrame['fun3_s']+dataFrame['amb3_s'])
	dataFrame['sinc3_s_x'] = dataFrame['sinc3_s']/(dataFrame['attr3_s']+dataFrame['sinc3_s']+dataFrame['intel3_s']+dataFrame['fun3_s']+dataFrame['amb3_s'])
	dataFrame['intel3_s_x'] = dataFrame['intel3_s']/(dataFrame['attr3_s']+dataFrame['sinc3_s']+dataFrame['intel3_s']+dataFrame['fun3_s']+dataFrame['amb3_s'])
	dataFrame['fun3_s_x'] = dataFrame['fun3_s']/(dataFrame['attr3_s']+dataFrame['sinc3_s']+dataFrame['intel3_s']+dataFrame['fun3_s']+dataFrame['amb3_s'])
	dataFrame['amb3_s_x'] = dataFrame['amb3_s']/(dataFrame['attr3_s']+dataFrame['sinc3_s']+dataFrame['intel3_s']+dataFrame['fun3_s']+dataFrame['amb3_s'])
	
	dataFrame['attr3_s_x'] = dataFrame['attr3_s_x']*100
	dataFrame['sinc3_s_x'] = dataFrame['sinc3_s_x']*100
	dataFrame['intel3_s_x'] = dataFrame['intel3_s_x']*100
	dataFrame['fun3_s_x'] = dataFrame['fun3_s_x']*100
	dataFrame['amb3_s_x'] = dataFrame['amb3_s_x']*100
	
	dataFrame.insert(10,'partnerSelfConfidence',int)
	dataFrame['partnerSelfConfidence'] = dataFrame['attr3_1'] + dataFrame['sinc3_1'] + dataFrame['fun3_1'] + dataFrame['intel3_1']+ dataFrame['amb3_1']
	dataFrame['partnerSelfConfidence'] = dataFrame['partnerSelfConfidence']/6
	dataFrame.insert(10,'subjectSelfConfidence',int)
	dataFrame['subjectSelfConfidence'] = dataFrame['attr3_s'] + dataFrame['sinc3_s'] + dataFrame['fun3_s'] + dataFrame['intel3_s']+ dataFrame['amb3_s']
	dataFrame['subjectSelfConfidence'] = dataFrame['subjectSelfConfidence']/6
	dataFrame = dataFrame.round({'subjectSelfConfidence':0, 'partnerSelfConfidence':0})
	
	
	dataFrame = dataFrame.drop("attr3_1", 1)
	dataFrame = dataFrame.drop("sinc3_1", 1)
	dataFrame = dataFrame.drop("intel3_1", 1)
	dataFrame = dataFrame.drop("amb3_1", 1)
	dataFrame = dataFrame.drop("fun3_1", 1)
	
	dataFrame = dataFrame.drop("attr1_s", 1)
	dataFrame = dataFrame.drop("sinc1_s", 1)
	dataFrame = dataFrame.drop("intel1_s", 1)
	dataFrame = dataFrame.drop("amb1_s", 1)
	dataFrame = dataFrame.drop("fun1_s", 1)
	
	dataFrame = dataFrame.drop("pf_o_att", 1)
	dataFrame = dataFrame.drop("pf_o_sin", 1)
	dataFrame = dataFrame.drop("pf_o_int", 1)
	dataFrame = dataFrame.drop("pf_o_fun", 1)
	dataFrame = dataFrame.drop("pf_o_amb", 1)
	dataFrame = dataFrame.drop("pf_o_sha", 1)
	
	dataFrame = dataFrame.drop("attr3_s", 1)
	dataFrame = dataFrame.drop("sinc3_s", 1)
	dataFrame = dataFrame.drop("intel3_s", 1)
	dataFrame = dataFrame.drop("amb3_s", 1)
	dataFrame = dataFrame.drop("fun3_s", 1)
	
	
	filename = "updated.csv"
	for index,row in dataFrame.iterrows():
		if row['match'] == 0:
			row['match'] = 'no'
		else:
			row['match'] == 'yes'1``
			
		
	"""
	
	#print(dataFrame["attr1_s"][0])
	for row in dataFrame["attr1_s"]:
		if(row == "nan"):
			print("fdsaklfjasfsdaieruiowu")

	for column in dataFrame:
		#print(dataFrame[column].isnull().sum())
		#modeValue = dataFrame[column].mode()
		print(modeValue)
		dataFrame = dataFrame[column].fillna(modeValue)
	"""
	dataFrame.to_csv(filename)
	"""
	dataFrame = dataFrame.sort_values(by=['field'])
	print(dataFrame["field"].unique())
	dataFrame = dataFrame.sort_values(by=['career'])
	print(dataFrame["career"].unique())
	"""
	
main()