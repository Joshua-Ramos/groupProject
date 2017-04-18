import re

#Checks if the given username is acceptable
#Username must only have dashes, underscore, and alphanumeric and be within 7o to 24 chars
def acceptable_username(username):
    username_length = len(username)
    acceptable_chars = re.search("^[A-Za-z0-9_-]*$", username)
    #print(bool(acceptable_chars))    
    return username_length > 6 and username_length < 25 and bool(acceptable_chars)


#Checks if the given password is acceptable
#Password must be between 12 and 99 chars and alphanumeric, underscore, and dashes

def acceptable_password(password):
    password_length = len(password)
    acceptable_chars = re.match("^[A-Za-z0-9_-]*$", password)
    return password_length > 11 and password_length < 100 and bool(acceptable_chars)


