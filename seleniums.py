from selenium import webdriver
from time import sleep
from pprint import pprint
import string
a=webdriver.Chrome()
a.maximize_window()
a.get("https://www.zomato.com/dharamshala")
sleep(5)
a.find_element_by_xpath("//input[@id='keywords_input']").send_keys("dinner")
# a.find_element_by_xpath("//input[@id='keywords_input']").send_keys("dinner")
# sleep(3)
a.find_element_by_xpath("//div[@role='button']").click()
def ajith():
	z={}
	q=[ ]
	name=a.find_elements_by_xpath("//a[@class='result-title hover_feedback zred bold ln24   fontsize0 ']")
	couisines=a.find_elements_by_xpath('//*[@id="orig-search-list"]/div[1]/div[1]/div/article/div[3]/div[1]/span[2]/a')
	address=a.find_elements_by_xpath("//div[@class='col-m-16 search-result-address grey-text nowrap ln22']")
	cash=a.find_elements_by_xpath("//span[@class='col-s-11 col-m-12 pl0']")
	time=a.find_elements_by_xpath("//div[@class='res-timing clearfix']")
	rate=a.find_elements_by_xpath("//div[@data-variation='mini inverted']")
	for j,i,k,l,m in zip(address,name,cash,rate,time):
		z["name"]=j.text	
		z["address"]=i.text
		z["cash"]=k.text
		z["rate"]=l.text
		z["time"]=m.text.strip("HOURS:").strip("\n")
		# q.append(z)
		pprint(z)
num=a.find_element_by_xpath("//div[@class='col-l-4 mtop pagination-number']")
lis=(num.text).split(" ")
# print(lis[-1])

for i in range(int(lis[-1])-1):
	ajith()
	a.find_element_by_xpath("//a[@class='paginator_item   next item']").click()
	sleep(5)