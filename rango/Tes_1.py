from google import google
num_page = 3
search_results = google.search("This is my query", num_page)
print(type(search_results))