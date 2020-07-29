import requests
def send_simple_message():
    response = requests.post(
		"https://api.mailgun.net/v3/sandbox4c51efabdf6644a9923f750895bc25c7.mailgun.org/messages",
		auth=("api", "9b1e4682a4a744f2bfb7ff9d42181c6e-a65173b1-e904236d"),
		data={"from": "Excited User <mailgun@sandbox4c51efabdf6644a9923f750895bc25c7.mailgun.org>",
			"to": ["alannavaseg_02@hotmail.com", "YOU@YOUR_DOMAIN_NAME"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})
    print (response.text)
    # print (response.__dict__)
    # print (response.headers)
    # print (response.__sizeof__)
    return response
send_simple_message()