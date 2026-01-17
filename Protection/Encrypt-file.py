# fonction HASH et AES
from pyAesCrypt import encryptFile
from pyAesCrypt import decryptFile
from os import remove
import hashlib
select = '''
[===========================================]
[ Sleect 1/ - HASH 2/ -Encrypt  3/ -Decrypt ]
[===========================================]'''
file = input("Enter File To Cryp AES:") 
nfile = file + ".aes"
print(select)
opt = input('#? ')
if opt == '1' :
    md5 = hashlib.md5()
    sh1 = hashlib.sha1()
    sh224 = hashlib.sha224()
    sh256 = hashlib.sha256()
    sh384 = hashlib.sha384()
    sh512 = hashlib.sha512()  
    list_hash = [md5 , sh1 , sh224 , sh256 ,sh384 , sh512]
    path = input('Enter File To Hash :')
    with open(path, 'rb') as f :
        print('result')
        print()
        content = f.read()
        for hash_c in list_hash :
            hash_c.update(content)
            print('{}:{}'.format(hash_c.name ,hash_c.hexdigest()))
# for large file may be 2 giga or larger
    # for hash_c in list_hash:
    #    with open(path, 'rb') as f :
    #        for line in f:
    #            hash_c.update(line)
    #            print('{}:{}'.format(hash_c.name ,hash_c.hexdigest()))
size = 64 * 1024
#passw = '12'
if opt == '2':
    passw = input("Enter Password To Encrypt:")
    encryptFile(file , nfile , passw ,size)
    remove(file)
    print('\033[31mDone File Is Encrypted')

if opt == '3' :
    passw = input("Enter Password To Decrypt:")
    decryptFile(nfile , file , passw , size)
    remove('path/file.aes')
    print('\033[32mDone File Is Decrypted')