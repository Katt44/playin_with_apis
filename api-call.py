"""Using Twilio, sends sms message"""

from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER

# add one of you phone numbers here with no spaces
# exampe: "+15553334444"
to_number = "+1 415-713-2720"
AUTH_TOKEN = "ca81013e0354d2ab9d68b251836ea578"
ACCOUNT_SID = "AC5f6da443fc06ba955486703c0ab93dd1"
# set a variable call client to an instance of Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# lets make and send the message, add in the missing data
message = client.api.account.messages.create(
                to=to_number,
                from_="+1 415-212-6943",
                body="You did it!")

print "Message set. Message Id: {}".format(message.sid)
