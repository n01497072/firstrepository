import requests
city = 'jalandhar'
api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': '3DmrUiA9RfyUmS1o/lBzdQ==xeFD7NjhoBZ4wyKW'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
