##XOR each character in input file is XOR'd with the KEY

decoded = ""
file = open("fileInput", "rb").read() ##open file for reading in binary mode

for c in file:
	decoded = decoded + chr(ord(c) ^ ord('KEY'))
	##chr converts integer value to ASCII
	##ord is inverse of chr