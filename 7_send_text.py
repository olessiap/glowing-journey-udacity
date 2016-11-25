from twilio.rest import TwilioRestClient

account_sid = "ACe32a5e1dc1507194591ba5683c9d94ba"
auth_token = "aad06830a1966b712a5e567cf0be7e23"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "this text was sent from Olessia's Mac",
    to = "+19258177675",
    from_="+1925901053")
print message.sid
