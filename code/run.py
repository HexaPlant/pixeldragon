from tasks import *

url="http://cdn.eso.org/images/screen/eso0202a.jpg"
oid="e0202a"

#print (add.delay(4,4))
print (fetch.delay(url,oid))
#print (process.delay(oid))
