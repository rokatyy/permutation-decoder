import sys
from permutation import decoding,encoding
def exception():
	print("Smth wrong, try to help")
	
if __name__=="__main__":
	print("permutation cipter decoding..")
	try:
		if sys.argv[1] == '-e':
				string = open(sys.argv[2],'r').read()
				f = open(sys.argv[3],'w')
				f.write(encoding(string,sys.argv[4]))
				f.close()		
		elif sys.argv[1] == '-d':			
				string = open(sys.argv[2],'r').read()
				decoding(string, sys.argv[3])
		else:
			print(open("help.txt","r").read())
	except:
		exception()
	
			