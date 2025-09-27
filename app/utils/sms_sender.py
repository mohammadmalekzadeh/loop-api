from app.core.config import SMS_API, SMS_SENDER
import json
import http

def sms_sender(phone, message):
    conn = http.client.HTTPSConnection("api.sms.ir")
    payload = json.dumps({
      "lineNumber": SMS_SENDER,
      "messageText": message,
      "mobiles": [phone],
      "sendDateTime": None
    })
    headers = {
      'X-API-KEY': SMS_API,
      'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/send/bulk", payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    return {"response": data.decode("utf-8")}