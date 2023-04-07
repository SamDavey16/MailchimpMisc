import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import pandas
import hashlib

df = pandas.read_csv("NZ_Mailchimp_data.csv")

for index, row in df.iterrows():
    try:
      client = MailchimpMarketing.Client()
      client.set_config({
        "api_key": "CHANGE ME",
        "server": "us3"
      })

      response = client.lists.delete_list_member_permanent("CHANGE ME", hashlib.md5(row["Card_Holder_Email"].encode()).hexdigest())
      print(response)
    except ApiClientError as error:
      print("Error: {}".format(error.text))
