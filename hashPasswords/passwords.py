from hashlib import sha512

def hashPassword( password, username ):
    return sha512('assystedisomgsogreat'+password+username).hexdigest()
