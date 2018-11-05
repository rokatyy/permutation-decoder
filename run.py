import sys
from permutation import decoding

if __name__=="__main__":
	print("permutation cipter decoding..")
	try:
		if sys.argv[1] == '-h' or sys.argv == '--help':
			print(open("help.txt","r").read())
		
		else:
			try: 
				string = open(sys.argv[1],'r').read()
				decoding(string, sys.argv[2])
			except:
				print("Smth wrong, try to help")
	except:
		print("Smth wrong, try to help")
	
			