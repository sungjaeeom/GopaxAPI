#
# Place order
#
import time, base64, hmac, hashlib, requests, json

# Use your API key and the secret
apikey = ''
secret = ''

# Generate nonce
nonce = str(time.time())
method = 'POST'
request_path = '/orders'

request_body = {
	"amount": 1.0,
	"price": 1.0,
	"side": "buy", #buy 또는 sell
	"tradingPairName": "CND-KRW",
	"type": "limit" #limit or market
};

# Generate prehash string
what = nonce + method + request_path + json.dumps(request_body,sort_keys=True)
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
	# method = post
	req = requests.post(url = 'https://api.gopax.co.kr' + request_path, headers = custom_headers,json=request_body)

	if req.ok:
		HTMLsouceGet(req)

	else:
		print ('Request error')
		HTMLsouceGet(req)
 
if __name__ == '__main__':
	main()
