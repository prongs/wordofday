import urllib2,re,datetime,glob,os



reldata=""

proxyinfo=open("proxy.txt")



wordpage=None
datestr=str(datetime.date.today())

todayfile=glob.glob(".\database\\"+datestr+"*")

proxy_handler = urllib2.ProxyHandler({'http': 'http://10.10.78.22:3128'})
proxy_auth_handler = urllib2.HTTPBasicAuthHandler()
#proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
#opener.open('http://www.stackoverflow.com')
l=proxyinfo.readline();
#print l
openfun=None
if l=='1' :
	print "opener.open"
	openfun=opener.open
	#print openfun
else :
	print "urllib2.urlopen"
	openfun=urllib2.urlopen
	#print openfun
	
print openfun
if len(todayfile)==0:	
	try : 
		wordpage=openfun("http://wordsmith.org/words/today.html")
	except Exception:
		print("unable to retrive word for today\n\n\nException: ")
		
	else:
		pagedata=wordpage.read()
		print("got the word")
#		print pagedata
		x=re.search(r'<h3>.*<rightlinks>', pagedata, re.DOTALL)
		xx=x.group(0)
		reldata=re.search(r'(.*)</td>.*', xx, re.DOTALL).group(1)
		title=re.search(r'<h3>(.*)\n</h3>.*', reldata, re.DOTALL).group(1)
		
		
		
		
		todaywordfile=open(".\database\\"+datestr+"-"+title.strip()+".wod","w")
		print >>todaywordfile, reldata
		todaywordfile.close()
		os.system("java Main "+".\database\\"+datestr+"-"+title.strip()+".wod")
else:
	twf=open(todayfile[0])
	reldata=twf.read()
	title=re.search(r'<h3>(.*)</h3>.*', reldata, re.DOTALL).group(1)
	os.system("java Main "+todayfile[0])
	