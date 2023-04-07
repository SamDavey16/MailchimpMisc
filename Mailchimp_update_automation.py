import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import hashlib
import pandas

df = pandas.read_csv("NZ_Mailchimp_data.csv")

for index, row in df.iterrows():
    try:
      client = MailchimpMarketing.Client()
      client.set_config({
        "api_key": "CHANGE ME",
        "server": "CHANGE ME"
      })

      response = client.lists.update_list_member("CHANGE ME", hashlib.md5(row["CHANGE ME"].encode()).hexdigest(), {"merge_fields": {"FNAME": row["CHANGE ME"]}})
      print(response)
    except ApiClientError as error:
      print("Error: {}".format(error.text))
