from datetime import datetime

now = datetime.now()
print (now)
dst = now.timestamp()
print(dst)
now = datetime.fromtimestamp(dst)
print(now)