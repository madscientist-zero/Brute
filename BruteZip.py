import os
def cls():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])
cls()
print '\033[31m'+'https://github.com/madscientist-zero'
print ''
print '\033[34m'+'####################################'
print '\033[31m' + '[1] Zip Password Cracker\n'
print '[0] Exit\n'

a=input(" Enter Number [0,1]: ")
if a==0:
 import os
 cls()
 print " see you:v"
 quit()
elif a==1:
 #!/usr/bin/python

 import zipfile
 import os
 from time import time
 
 cls()
 print '\033[31m'+'https://github.com/madscientist-zero'
 print 'BruteZip'
 print '\033[34m'+'###################################'
 print ''
 file_path = raw_input ('\033[96m'+'ZIP File Address: ')
 print ""
 word_list = raw_input ('\033[34m'+'Password.txt Address: ')
 def main(file_path, word_list):
	try:
		zip_ = zipfile.ZipFile(file_path)
	except zipfile.BadZipfile:
		print '\033[34m' + 'Its not a ZIP file.'
		quit()

	password = None 
	i = 0 
	c_t = time()
	with open(word_list, "r") as f: 
		passes = f.readlines() 
		for x in passes:
			i += 1
			password = x.split("\n")[0]  
			try:
				zip_.extractall(pwd=password)
				t_t = time() - c_t 
				print "\n Password Found;v\n" + " [*] Password: "+password+"\n" 
				print " %f seconds to rack the Password. That is, %i attempts per second." % (t_t,i/t_t)
				quit()
			except Exception:
				pass
		print '\033[36m'+'Password Not Found'
		quit()
 main(file_path, word_list)
