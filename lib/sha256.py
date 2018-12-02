import hashlib

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
if __name__=='__main__':
    hash_string = 'confidential data'
    sha_signature = encrypt_string(hash_string)
    print(sha_signature)
