from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
count = 0

df = pd.DataFrame(columns=['Brands', 'Year', 'Condition', 'Dealer_Name', 'City_State', 'Zip', 'Phone'])


def getInfo(url_s):
	try:	
		arr = list()
		page_s = urlopen(url_s)
		soup_s = BeautifulSoup(page_s, features="lxml")
	except:
		print("link broken")
	try:
		item1 = soup_s.find("h1", class_ = "vehicle-info__title")
		arr.append(str(item1.text)[6:].strip())
		arr.append(str(item1.text)[:5].strip())
		# print(str(item1.text).strip())
	except:
		print("Data missing item1")
		arr.append('-')
	try:
		item2 = soup_s.find("h1", class_ = "vehicle-info__stock-type")
		arr.append(str(item2.text).strip())
		# print(str(item2.text))
	except:
		print("Data missing item2")
		arr.append('-')
	try:
		item3 = soup_s.find("h2", class_ = "page-section__title")
		arr.append(str(item3.text)[8:].strip())
		# print(str(item3.text)[8:])
	except:
		print("Data missing item3")
		arr.append('-')
	try:
		item4 = soup_s.find("a", class_ = "get-directions-link__link")
		location = str(item4.text).strip().split(', ')
		arr.append(location[0])
		arr.append(location[1])
		# print(location)
	except:
		print("Data missing item4")
		arr.append('-')
	try:
		item5 = soup_s.find("div", class_ = "vdp-cap-seller-exp__phone")
		st1 = str(item5.text).strip().split(' ')
		st1 = st1[1]+st1[2]
		arr.append(st1)
		# print(st1)
	except:
		print("Data missing item5")
		arr.append('-')


	return arr

def addItems(ary):
	global df, count
	df = df.append({'Brands' : ary[0] , 'Year' : ary[1], 'Condition' : ary[2], 'Dealer_Name': ary[3], 
					'City_State': ary[4], 'Zip': ary[5], 'Phone': ary[6]} , ignore_index=True)
	print("item added ",count)
	count+=1



url = "https://www.apartments.com/louisville-ky/?bb=wjylpzr6_I0o648vvG"
print("."*2)
page = urlopen(url)
print("."*4)
soup = BeautifulSoup(page, features="lxml")
print("."*8)

getAll = soup.find_all("article", class_ = "diamond placard")
print("."*16)
# for i in getAll:
# 	url_items = "https://www.cars.com" + str(i['href'])
# 	arry = getInfo(url_items)
# 	addItems(arry)
print(getAll[0])

# df.to_csv("Cars.csv",index = None, header=True)

# print(getInfo("https://www.cars.com/vehicledetail/detail/773079000/overview/"))





	# df = df.append({'Brands' : ary[0]} , ignore_index=True)
	# df = df.append({'Year' : ary[1]}, ignore_index=True)
	# df = df.append({'Condition' : ary[2]}, ignore_index=True)
	# df = df.append({'City_State': ary[4]}, ignore_index=True)
	# df = df.append({'Zip': ary[5]}, ignore_index=True)
	# df = df.append({'Phone': ary[6]} , ignore_index=True)