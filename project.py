from urllib.request import urlopen
from bs4 import BeautifulSoup


webpage = 'https://coinmarketcap.com/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)



crypto_rows = soup.findAll('tr')

for x in range(1,6):
    td = crypto_rows[x].findAll('td')
    name = crypto_rows[x].findAll('td')
    current_price = crypto_rows[x].findAll('td')
    change = crypto_rows[x].findAll('td')
    print(td[1].text)
    print(name[2].text)
    print(current_price[3].text)
    print(change[7].text)
    

    if name == 'Bitcoin' and current_price < 40000:
        print(f'Bitcoin has dropped to {current_price}')

    if name == 'Ethereum' and current_price < 3000:
        print(f'Ethereum has dropped to {current_price}')

'''

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = '+17432026208'

myCellPhone = '+18304817381'


textmessage = client.messages.create(to=myCellPhone,from_TwilioNumber, body=current_price)


'''














