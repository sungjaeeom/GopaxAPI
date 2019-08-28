#
# Get order
#
import time, base64, hmac, hashlib, requests, json

# Use your API key and the secret
apikey = ''
secret = ''

# Generate nonce
nonce = str(time.time())
method = 'GET'
request_path = '/orders'

# Generate prehash string
what = nonce + method + request_path
# Decode the secret using base64
key = base64.b64decode(secret)
# Generate the signature using HMAC
signature = hmac.new(key, str(what).encode('utf-8'), hashlib.sha512)
# Finally, Encode the signature in base64
signature_b64 = base64.b64encode(signature.digest())

# Get HTML source
def HTMLsouceGet(p):
	print (p.text)
	
custom_headers = {
	'API-Key': apikey,
	'Signature': signature_b64,
	'Nonce': nonce
}
								
def main():
	# method = get
	req = requests.get(url = 'https://api.gopax.co.kr' + request_path, headers = custom_headers)

	if req.ok:
		HTMLsouceGet(req)

	else:
		print ('Request error')
		HTMLsouceGet(req)
 
if __name__ == '__main__':
	main()
