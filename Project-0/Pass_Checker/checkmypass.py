import hashlib
import requests
import sys

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code > 200:
        raise RuntimeError(f"error fetching : {res.status_code} is higher than expected please try again")
    return res

def get_pass_leaked_out(hashes , hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h,count in hashes:
       if h == hash_to_check:
        return count
    return 0

def pwend_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char,tail = sha1password[0:5],sha1password[5:]
    response = request_api_data(first5_char)
    #print(first5_char, tail)
    print (response)
    return get_pass_leaked_out(response , tail)

def main(args):
    for password in args:
        count = pwend_api_check(password)
        if count :
            print(f"your {password} is {count} times hacked")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))