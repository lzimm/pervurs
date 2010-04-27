import cPickle
from StringIO import StringIO
from Crypto.Cipher import ARC4
from pervurs.settings import SECRET_KEY
from pervurs.models import User
from twisted.web2.http_headers import Cookie
from pervurs.libs.qonvo.auth import validate

def auth(req):
    req.cookies = []
    req.user = None

    qonvo_auth = None
    qonvo_uid = None
    auth_cookie = None
    
    cookies = req.headers.getHeader('cookie', [])
    
    if cookies:
        for cookie in cookies:
            if cookie.name == 'qonvo_auth':
                qonvo_auth = cookie.value
            elif cookie.name == 'qonvo_id':
                qonvo_uid = cookie.value
            elif cookie.name == 'auth':
                try:                
                    data = StringIO(ARC4.new(SECRET_KEY).decrypt(cookie.value.decode('base64')))
                    row = cPickle.load(data)
                    user = User(row)
                    data.close()
       
                    if row['ip'] == req.remoteAddr.host:
                        req.user = user                     
                except:
                    pass
    
        if getattr(req.user, 'id', None) != qonvo_uid:
            req.user = None
            auth_cookie = Cookie('auth','',path='/')
        elif req.user:
            return None
    
    if qonvo_auth and qonvo_uid:
        validated = validate(qonvo_auth, qonvo_uid)
        if validated:
            validated['ip'] = req.remoteAddr.host
        
            dump = StringIO()
            cPickle.dump(validated, dump)
            data = dump.getvalue()
            dump.close()

            auth = ''.join(ARC4.new(SECRET_KEY).encrypt(data).encode('base64').splitlines()).strip()
            auth_cookie = Cookie('auth',auth,path='/')

            req.user = User(validated)

    if auth_cookie:
        req.cookies.append(auth_cookie)

    return None