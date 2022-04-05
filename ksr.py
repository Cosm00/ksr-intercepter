from flask import Flask, jsonify, request, send_file, Response
import json, requests, threading
from io import StringIO

app = Flask(__name__)
cookieStrings = ''
atcCookieString = ''

@app.route('/api/receiveHeaders', methods = ['POST'])
def receiveHeaders():
    global cookieStrings, atcCookieString
    headers = []
    try:
        bodyData = json.loads(request.get_json()['DeviceInfo'])
    except:
        bodyData = None
    headers.append({
        "name" : "X-GyJwza5Z-z",
        "value" : request.get_json()['HeaderZ']
    })
    headers.append({
        "name" : "X-GyJwza5Z-f",
        "value" : request.get_json()['HeaderF']
    })
    headers.append({
        "name" : "X-GyJwza5Z-d",
        "value" : request.get_json()['HeaderD']
    })
    headers.append({
        "name" : "X-GyJwza5Z-b",
        "value" : request.get_json()['HeaderB']
    })
    headers.append({
        "name" : "X-GyJwza5Z-c",
        "value" : request.get_json()['HeaderC']
    })
    headers.append({
        "name" : "X-GyJwza5Z-a",
        "value" : request.get_json()['HeaderA']
    })
    try:
        headers.append({
            "name" : "X-GyJwza5Z-a0",
            "value" : request.get_json()['HeaderA0']
        })
    except:
        pass
    if bodyData == None:
        atcCookieString += str(json.dumps({
            "bodyData" : bodyData,
            "headers" : headers,
            "userAgent" : {
                "name" : "User-Agent",
                "value": request.get_json()['UserAgent']
            }
        })).replace('\n', '') + '\n'
    else:
        cookieStrings += str(json.dumps({
            "bodyData" : bodyData,
            "headers" : headers,
            "userAgent" : {
                "name" : "User-Agent",
                "value": request.get_json()['UserAgent']
            }
        })).replace('\n', '') + '\n'
    
    threading.Thread(target = passCookies, args = [request.get_json()]).start()

    print('Loaded Cookie')
    return ''

def passCookies(cookies):
    try:
        s = requests.Session()
        s.post('http://localhost:58770/api/receiveHeaders', json = cookies, timeout = 2)
        print('Pushed Cookie to KSR')
    except:
        pass

@app.route('/getCookies/login/stellar')
def loginStellar():
    global cookieStrings, atcCookieString
    buffer = StringIO()
    buffer.write(cookieStrings)
    file = buffer.getvalue()
    cookieStrings = ''
    return Response(file, mimetype="text/plain", headers = {"Content-disposition": "attachment; filename=output.txt"})

@app.route('/getCookies/cart/stellar')
def cartStellar():
    global cookieStrings, atcCookieString
    buffer = StringIO()
    buffer.write(atcCookieString)
    file = buffer.getvalue()
    cookieStrings = ''
    return Response(file, mimetype="text/plain", headers = {"Content-disposition": "attachment; filename=output.txt"})

print('''  _  __ _____ _____    _____ _   _ _______ ______ _____   _____ ______ _____ _______ 
 | |/ // ____|  __ \  |_   _| \ | |__   __|  ____|  __ \ / ____|  ____|  __ \__   __|
 | ' /| (___ | |__) |   | | |  \| |  | |  | |__  | |__) | |    | |__  | |__) | | |   
 |  <  \___ \|  _  /    | | | . ` |  | |  |  __| |  _  /| |    |  __| |  ___/  | |   
 | . \ ____) | | \ \   _| |_| |\  |  | |  | |____| | \ \| |____| |____| |      | |   
 |_|\_\_____/|_|  \_\ |_____|_| \_|  |_|  |______|_|  \_\\______|______|_|      |_|   
                                                                                     
                                                                                     
                                                                                     
      COOKIE INTERCEPTER LISTENING ON PORT 43287, PLEASE SEND COOKIES THERE...''')
app.run(host='0.0.0.0', port=43287)

