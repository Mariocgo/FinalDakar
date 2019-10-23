from twilio.rest import Client
import serial
import time
ser = serial.Serial('COM5', 9600)

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACbca67f19fe2e489825f274debea07132'
auth_token = 'bb5c134dd4c77aca46846ff098bbcef1'
client = Client(account_sid, auth_token)


while True:
    while ser.inWaiting():
        temp = ser.readline().decode()
        messageTosend=""+str(temp)+"."
        print(""+""+str(temp)+".")
        message = client.messages.create(
                              body=messageTosend,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+5219991483130'
                          )
        time.sleep(0)

print(message.sid)