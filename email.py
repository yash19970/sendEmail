#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
import requests
url = 'https://api.sendgrid.com/v3/mail/send'
payload = {
	"personalizations": [{"to": [{"email": "yashjain19970@gmail.com"}]}],
	"from": {"email": "yash19970@gmail.com"},
	"subject": "Hello, World!",
	"content": [{"type": "text/plain", "value": "Heya!"}] }
hdr = {'content-type': 'application/json', 'Authorization' : 'Bearer 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'}
r = requests.post(url, data=json.dumps(payload))
