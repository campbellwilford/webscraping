
from urllib.request import urlopen
from bs4 import BeautifulSoup






#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##


movie_rows = soup.findAll('tr')
#print(movie_rows)

for x in range(1,6):
    td = movie_rows[x].findAll('td')
    print(td[1].text)  









'''
movie_list = soup.findAll('table')


for list in movie_list(5):
    ml = list.findAll('ml')
    rank = ml[0].text
    release = int(ml[5].text.replace(',',''))
    theatre = int(ml[6].text.replace(',',''))
    gross = int(ml[7].text.replace(',',''))
    distributor = int(ml[8].text.replace(',',''))

    


    print(rank)
    print(f'Movie Realeased: {release}')
    print(f'Theatres: {theatres}')
    print(f'Total Gross: {gross}')
    print(f'Distributor: {distributor}')
    print(f'Average Revenue: {avg_revenue}')
    print()
    print()

    counter+=11
    


'''


