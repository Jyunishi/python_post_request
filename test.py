from urllib import request


API_URL = 'https://api.exmo.com/v1/'
GET_TRADES = 'trades/'
GET_STAT = 'ticker/'

# req_str = '?pair=BTC_USD'
# headers = {'pair': 'BTC_USD'}
#
# req_result = request.Request(API_URL + API_METHOD+req_str)
#
# with request.urlopen(req_result) as response:
#     api_answer = response.read()

req_result = request.Request(API_URL + GET_STAT)
with request.urlopen(req_result) as response:
    api_answer = response.read()

print(api_answer)
