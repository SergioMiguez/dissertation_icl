import requests

# URL of switch
base_url = 'http://192.168.1.43'

# keep cookies and credentials
session = requests.Session()

# Headers
common_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://192.168.1.43',
    'Referer': 'http://192.168.1.43/',
}

# Step 1: Authentication
login_url = f'{base_url}/logon.cgi'
login_data = {
    'username': 'admin',
    'password': '{   }',
    'cpassword': '',
    'logon': 'Login'
}

# Send request to start session
response = session.post(login_url, headers=common_headers, data=login_data)
print('Login response:', response.status_code, response.content)

# Verify if the login was successful and get H_P_SSID cookie
if response.status_code == 200 and 'Successful Login' in response.text:
    print('The login was successful')
else:
    print('Error the login failed')
