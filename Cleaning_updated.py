import re
import json
#Zhengyang_Zhou cleaning



# logline = '174.135.50.92 - - [05/Mar/2017:00:00:00 +0000] "GET /axis2/services/WebFilteringService/getCategoryByUrl?app=firefox_AntiPorn&ver=0.19.6.9&url=http%3A%2F%2Ftpc.googlesyndication.com%2Fsodar%2FadXpYxnS.html&cat=business-and-economy HTTP/1.1" 200 133 "-" "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"'
#
# str = re.split('\s|&|\"|\'|\?',logline)
# print str


f = open('/Users/zhengyjo/Desktop/DS501/CAPSTONE/2017_log_test.json', 'w')
count=0
jsonDict={}
#with open('/Users/zhengyjo/Desktop/DS501/CAPSTONE/unit_test.txt', 'r') as file:
with open('/Users/zhengyjo/Desktop/DS501/CAPSTONE/unit_test.txt','r') as file:
    for line in file:

        ip=''
        time =''
        serverUrl=''
        #app=''
        browser=''
        api=''
        ver=''
        url=''
        cat=''
        HTTP =''
        passSignal1=''
        passSignal2=''
        pretend=''
        str = re.split('- -|\&|\"|\'|\?', line)
        for part in str:
            if(re.match(r"[0-9]+(?:\.[0-9]+){3}",part)):
                ip=re.sub('\s','',part)
            elif('[' in part and ']' in part):
                time = re.sub('\[|\]|\s|\+0000','',part)
            elif('GET' in part):
                serverUrl = re.sub('GET ','',part)
            elif ('app=' in part):
                part = re.sub('app=', '', part)
                if ('_' in part):
                    partSub = re.split('_', part)
                    browser = partSub[0]
                    api = partSub[1]
            # elif ('url=' in part or 'uri=' in part):
            #     url = re.sub('url=|uri=', '', part)
            elif ('cat=' in part):
                if ('HTTP' in part):
                    partSub = re.split('\s', part)
                    for partPart in partSub:
                        if ('cat' in partPart):
                            cat = re.sub('cat=', '', partPart)
                        elif ('HTTP' in partPart):
                            HTTP = partPart
                else:
                    cat = re.sub('cat=', '', part)
            elif ('HTTP' in part):
                if ('key' in part):
                    partSub = re.split('\s', part)
                    for partPart in partSub:
                        if ('HTTP' in partPart):
                            HTTP = re.sub('cat=', '', partPart)
            elif ('ver=' in part):
                ver = re.sub('ver=', '', part)

            # elif (re.match(r"\s[0-9]+(?:\s[0-9]+){1}\s", part)):
            #     passSignal1=re.sub('\s','',part[:4])
            #     passSignal2=re.sub('\s','',part[5:])
            # elif(str.index(part)==(len(str)-2)):
            #     pretend =part
            #     print pretend

        dict = {'ip':ip,
                'time':time,
                #'serverUrl':serverUrl,
                'browser':browser,
                'api':api,
                'ver':ver,
                #'url':url
                'cat':cat
                #'HTTP':HTTP
                #'passSignal1':passSignal1,
                #'passSignal2':passSignal2,
                #'pretend':pretend
                }
        count += 1
        jsonDict[count] = dict



json.dump(jsonDict, f, sort_keys=True, indent=4, separators=(',', ': '))

file.close()
f.close()