

# from requests_html import HTMLSession

# def weather():
#     s = HTMLSession()
#     query = "patna"
#     url = f'https://www.google.com/search?q=weather+{query}'
    
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
#     }
    
#     # Get the webpage
#     r = s.get(url, headers=headers)
    
#     # Extract the required information
#     try:
#         temp = r.html.find('span#wob_tm', first=True).text
#         unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
#         desc = r.html.find('span#wob_dc', first=True).text
        
#         # Return formatted weather information
#         return f"{temp} {unit}, {desc}"
#     except AttributeError:
#         return "Could not fetch weather details. Please check the query or the page structure."

# # Example call
# print(weather())

from requests_html import HTMLSession

def weather(query="patna"):
    url = f"https://www.google.com/search?q=weather+{query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    try:
        session = HTMLSession()
        response = session.get(url, headers=headers)
        temp = response.html.find('span#wob_tm', first=True).text
        unit = response.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
        desc = response.html.find('span#wob_dc', first=True).text
        return f"{temp}{unit}, {desc}"
    except Exception as e:
        return f"Error fetching weather: {e}"

print(weather())

