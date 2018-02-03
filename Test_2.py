from py_bing_search import PyBingWebSearch
term='SDU'
bing_web=PyBingWebSearch('0058bb2e43054214a2ce6d39539b57b5',term,web_only=False)

first=bing_web.search(limit=50,format='json')

print(type(first))