import hashlib
import sys,os

class Hex_digest:
    def __init__(self):
        self.print_banner()
        self.hash_key = str(input('Enter the hash algo name: '))

        self.file_path = str(input('Enter the file name or path: >>> '))

        self.hash_to_decrypt = str(input('Enter Hash Word'))
        self.algo_check()

    def banner(self):

        Banner = '''
        
                   _   _           _          _ _                 _            
| | | |         | |        | (_)               | |           
| |_| | __ _ ___| |__    __| |_  __ _  ___  ___| |_ ___ _ __ 
|  _  |/ _` / __| '_ \  / _` | |/ _` |/ _ \/ __| __/ _ \ '__|
| | | | (_| \__ \ | | || (_| | | (_| |  __/\__ \ ||  __/ |   
\_| |_/\__,_|___/_| |_| \__,_|_|\__, |\___||___/\__\___|_|   
                    ______       __/ |                       
                   |______|     |___/                            
        
        developed by Dhanajay Meshram
        year 2021
        
         +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |d|e|c|r|y|p|t|s| |*|s|h|a|1|,|m|d|5|,|s|h|a|2|2|4|,|s|h|a|2|5|6|,|s|h|a|3|8|4|*|
 +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        
        '''

        return Banner

    def print_banner(self):
        banner = self.banner()
        print(banner)

    def algo_check(self):
        Algo = ['sha1','sha224','md5','sha256','sha384']
        if self.hash_key in Algo:
            pass
        else:
            print('Ivalid algo name supplied')

    def file_verify(self):
        if os.path.exists(self.file_path):
            self.cracker()

        else:
            print('Invalid path!'+self.file_path)
            sys.exit()

    def cracker(self):
        with open(self.file_path, 'r') as file:
            for lines in file.readlines():
                if self.hash_key == 'md5':
                    hash_obj = hashlib.md5((lines.strip().encode()))
                    hash_word = hash_obj.hexdigest()
                    if self.hash_to_decrypt == hash_word:
                        print('Hash decrypted as: ' + lines.strip())
                        exit(0)
                elif self.hash_key == 'sha1':
                    hash_obj = hashlib.sha1((lines.strip().encode()))
                    hash_word = hash_obj.hexdigest()
                    if self.hash_to_decrypt == hash_word:
                        print('Hash decrypted as: ' + lines.strip())
                        exit(0)

                elif self.hash_key == 'sha224':
                    hash_obj = hashlib.sha224((lines.strip().encode()))
                    hash_word = hash_obj.hexdigest()
                    if self.hash_to_decrypt == hash_word:
                        print('Hash decrypted as: ' + lines.strip())
                        exit(0)

                elif self.hash_key == 'sha256':
                    hash_obj = hashlib.sha256((lines.strip().encode()))
                    hash_word = hash_obj.hexdigest()
                    if self.hash_to_decrypt == hash_word:
                        print('Hash decrypted as: ' + lines.strip())
                        exit(0)

                elif self.hash_key == 'sha384':
                    hash_obj = hashlib.sha384((lines.strip().encode()))
                    hash_word = hash_obj.hexdigest()
                    if self.hash_to_decrypt == hash_word:
                        print('Hash decrypted as: ' + lines.strip())
                        exit(0)





if __name__=='__main__':
    hex = Hex_digest()
    hex.file_verify()