//
// Place order
//
var crypto = require('crypto');
var request = require('request');

// Use your API key and the secret
var apikey = '';
var secret = '';

// Generate nonce
var nonce = Date.now() * 1000;
var method = 'POST';
var requestPath = '/orders';
var json_body = {
  amount: 1.0,
  price: 1.0,
  side: "buy", //buy or sell
  tradingPairName: "CND-KRW",
  type: "limit" //limit or market
};
var body = JSON.stringify(json_body, Object.keys(json_body).sort());

// Generate prehash string
var what = nonce + method + requestPath + body;
// Decode the secret using base64
var key = Buffer(secret, 'base64');
// Generate sha512 hmac using secret
var hmac = crypto.createHmac('sha512', key);

// Generate the signature using HMAC
// Finally, Encode the signature in base64
var sign = hmac.update(what).digest('base64');


var host = 'api.gopax.co.kr'; //Please check API endpoint

var options = {
  method,
  body: json_body,
  json: true,
  url: `https://${host}${requestPath}`,
  headers: {
    'API-KEY': apikey,
    Signature: sign,
    Nonce: nonce
  },
  strictSSL: false,
};

request(options, (err, response, b) => {
  if (err) {
    console.log('err:', err);
    return;
  }
  console.log(b);
});
