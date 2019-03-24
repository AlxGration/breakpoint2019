import json
import os

'''

 script for parse JSON-files into ONE training file

'''

path = os.getcwd()+"\\small_dataset"

#file with count sentence for different support data
ans = open(os.getcwd()+'\\ans.txt', 'w', encoding="utf-8")

#file with traing sentence
train_dir = open(os.getcwd() + "\\train_text.txt", 'w', encoding="utf-8") 

for folder in os.listdir(path):
	supFold = path + "\\" + folder
	print(supFold)

	os.chdir(supFold)

	# now in support folder
	cnt = 0
	for file in os.listdir(os.getcwd()):

		#open every JSON-file and read
		with open(file,  encoding='utf-8') as f:
		    data = json.load(f)

		# filling training file and count strings
		for mes in data['messages']:
			if (mes['sender'] == "user"):
				cnt += 1
				#
				train_dir.write(mes['message']+'\n')

	# write cnt of support sentence
	ans.write(str(cnt)+' ')


train_dir.close()
ans.close()