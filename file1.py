from bs4 import BeautifulSoup
import requests
import pandas as pd
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html')
table=soup.find_all('table')[0]
titles=table.find_all('th')
world_table_title=[title.text.strip() for title in titles]
#lets get rid og backslash n use strip for that
df=pd.DataFrame(columns=world_table_title)
#tr-rows and td-values in html
column_data=table.find_all('tr')
for row in column_data[1:]:
    # we are starting from 1 kyuki 0 valla null tha
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip() for data in row_data]
    length=len(df)
    df.loc[length]=individual_row_data 
print(df)
df.to_csv('structured_from.csv',index=False)
df.to_json('structured_form.json',index=False)
# now we have a structured form of table in structured_form_csv 
print(df.describe())

