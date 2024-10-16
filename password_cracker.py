import hashlib
print("*********************PASSWORD CRACKER**************************")
pass_found = 0
input_hash = input("Enter the hashed password: ")
pas_doc = input("Enter the path to the file: /home/serena/")
pass_doc = '/home/serena/' + pas_doc
try:
        pass_file = open(pass_doc,'r')
except:
        print("Error:")
        print(pass_doc,"is not found.\nPlease give the path of file correctly")
        quit()
for word in pass_file:
	enc_word = word.encode('utf-8')
	hash_word = hashlib.md5(enc_word.strip())
	digest = hash_word.hexdigest()
	if digest == input_hash:
		print("Password found. The password is:",word)
		print("****************************PASSWORD FOUND******************************")
		pass_found = 1
		break
if not pass_found:
        print("Password is not found. Sorry")

###To find the hash of a password, use the program below:
##import hashlib
##word = input()
##enc_word = word.encode()
##hash_word = hashlib.md5(enc_word.strip())
##password = hash_word.hexdigest()
##print(password)
