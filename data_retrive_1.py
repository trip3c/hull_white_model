import urllib2

############################################################
# Part 1: Build connection and get data
############################################################
query = 'On+random+graph'
url = 'http://scholar.google.com/scholar?hl=en&q=' + query + '&btnG=&as_sdt=1%2C5&as_sdtp='

header = {'Host': 'scholar.google.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive'}

req = urllib2.Request(url, headers = header)
con = urllib2.urlopen(req)

doc = con.read()

con.close()



############################################################
# Part 2: Analyze the data
############################################################
import BeautifulSoup
import re

soup = BeautifulSoup(doc)
paper_name = soup.html.body.find('h3', {'class' : 'gs_rt'}).text
paper_name = re.sub(r'\[.*\]', '', paper_name) # eliminate '[]' tags like '[PDF]'
paper_author = soup.html.body.find('div', {'class' : 'gs_a'}).text
paper_desc = soup.html.body.find('div', {'class' : 'gs_rs'}).text
temp_str = soup.html.body.find('div', {'class' : 'gs_fl'}).text
temp_re = re.match(r'[A-Za-z\s]+(\d*)[A-Za-z\s]+(\d*)', temp_str)
citeTimes = temp_re.group(1)
versionNum = temp_re.group(2)
if citeTimes == '':
	citeTimes = '0'
if versionNum == ''
	versionNum = '0'
citedPaper_href = soup.html.body.find('div', {'class' : 'gs_fl'}).a.attrs[0][1]



############################################################
# Part 3: Store the data
############################################################
file = open('webdata.txt','a')
line = paper_name + '#' + paper_author + '#' + paper_desc + '#' + citeTimes + '\n'
file = file.write(line)
file.close()



############################################################
# Part 4: Open database in cmd
############################################################
net start mysql55
net stop mysql55




############################################################
# Part 5: Open MySQL Modul
############################################################
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='yourPassword', db='dbname', port=3306, charset='utf8')
cur = conn.cursor()
cur.execute("select * from citeRelation where paperName = 'On Random Graph'")
list = cur.fetchall()
sql = "update studentCourseRecord set fail = 1 where studentID = '%s' and semesterID = '%s' and courseID = '%s'" %(studentID,course[0],course[1])
cur.execute(sql)
conn.commit()
cur.close()
conn.close()








