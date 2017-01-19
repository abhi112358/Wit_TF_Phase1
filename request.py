import requests




r=requests.get("https://api.wit.ai/message?v=20170111&q=Hello", headers={"Authorization":"Bearer QWRFP44Y7XSF3LNVOARB4RGLVCGHZSWH"})
print r.text
print r.status_code