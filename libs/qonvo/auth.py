import httplib, urllib
import simplejson as json

def login(email, password):
    try:
        params = json.dumps({'email': email, 'password': password})
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        conn = httplib.HTTPConnection("www.qonvo.com", 80)
        conn.request("POST", "/api/login", params, headers)
        response = conn.getresponse()
        
        data = response.read()

        conn.close()

        user = json.loads(data)['result']

        if user['id']:
            return user
    except:
        raise
    
    return None

def validate(auth, uid):
    try:
        params = json.dumps({'auth': auth, 'uid': uid})
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        conn = httplib.HTTPConnection("www.qonvo.com", 80)
        conn.request("POST", "/api/validate", params, headers)
        response = conn.getresponse()

        data = response.read()

        conn.close()
        
        user = json.loads(data)['result']

        if user['id']:
            return user
    except:
        pass
    
    return None