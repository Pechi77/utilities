import pandas as pd

""""
Sample data should look like this.

23/08/2021| DESIRE CHETTINAD RESTA |190.00|
27/08/2021| GOOGLE* Tekkullan Ltd |130.00|
04/09/2021| 995732 Payment Received Fund Transfer| 10.00 |CR
04/09/2021| 1554374 Payment Received Fund Transfer| 12.00 |CR
04/09/2021| YBL124716815081_Payment_Received_IMPS |71,781.00| CR
07/09/2021| PAYTM BUS |3,360.00|
09/09/2021| A and A NATURALS |2,791.00|
14/09/2021| SARAVANA STORES(TEX) T |222.00|

To do 

fetch last statement bill and deduct amount
"""


df = pd.read_clipboard(sep="|",header=None)

df_credit = df[df[3].str.strip().eq("CR")]

df_debit = df[df[3].str.strip().ne("CR")]

credited_amount = df_credit[2].str.replace(",","").astype(float).sum()

debited_amount = df_debit[2].str.replace(",","").astype(float).sum()

debited_amount

debited_amount - 22



