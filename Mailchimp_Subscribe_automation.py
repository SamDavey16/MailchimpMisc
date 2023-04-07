import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import pandas

df = pandas.read_csv("NZ_Mailchimp_data.csv")

for index, row in df.iterrows():
    try:
      client = MailchimpMarketing.Client()
      client.set_config({
        "api_key": "CHANGE ME",
        "server": "CHANGE ME"
      })

      response = client.lists.add_list_member("CHANGE ME", {"email_address": row["CHANGE ME"], "status": "subscribed", "name": row["CHANGE ME"]})
      print(response)
    except ApiClientError as error:
      print("Error: {}".format(error.text))
