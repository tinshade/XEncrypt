import os
class XEncrypt():
	#Encrypting Files
	def encFiles(path,key):
		"""
			Encrypts the file and replaces the original with the encrypted version.
		"""
		target_file=open(path, 'rb')
		data = target_file.read()
		target_file.close()
		data = bytearray(data)
		for i,v in enumerate(data):
			data[i] = v ^ key #XOR with the value for encrytion

		#Writing the encryption back to the disk
		os.remove(path) #remove the original
		root_path=path.split(".")
		ext = ""
		for each in root_path[1]:
			ext+= str(ord(each))+"$"
		encrypted_file = open(root_path[0]+"@"+ext+".xer", 'wb')
		encrypted_file.write(data)
		print("\nYour file has been encrypted successfully!\n")
		return
	#Decrypting Files
	def decFiles(path,key):
		"""
			Decrypts the file if the key was valid and replaces the encrypted version with the decrypted one.
		"""
		file=open(path, 'rb')
		data = file.read()
		file.close()
		data = bytearray(data)
		for i,v in enumerate(data):
			data[i] = v ^ key #XOR with the value for encrytion

		#Writing the encryption back to the disk
		file_ext = path.split(".")[0].split('@')[1]
		file_ext = file_ext[:len(file_ext)-1]
		file_ext = file_ext.split("$")
		og_ext = "."
		for i in range(len(file_ext)):
			og_ext += chr(int(file_ext[i]))
		try:
			dec_path = path.split('@')
			os.remove(path) #Remove the encrypted version
			file = open(dec_path[0]+og_ext, 'wb')
			file.write(data)
		except:
			#todo: 1 Maintained SHA checksum in dict file in a pickle
			print("\nThe file/extension is corrupt. Decryption failed!\n")
			return
	def main():
		"""
			Driver method for the program. Takes input and cleans it up before calling other functions
		"""
		try:
			key = abs(int(input("\nEnter a key between 1-255:\n")))
			abspath = input("Enter the path of your file: ")
			if os.path.exists(abspath):
				ext = abspath.split(".")[1]
				if ext == 'xer':
					XEncrypt.decFiles(abspath, key)
				else:
					XEncrypt.encFiles(abspath, key)
				print("Kudos!\nCleaning up and exiting now.. \n")
				exit()
			else:
				print("\nPlease ensure the file/path exists and try again!\n")
		except:
			return("\nThe value must be between 1 and 255!\n")

	

if __name__ == "__main__":
	XEncrypt.main()
else:
	print("\nImporting is not supported. Run the file directly!\n")
	exit()
