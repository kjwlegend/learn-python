from requests_html import HTMLSession

session = HTMLSession()

print(session)
print(type(session))

r = session.get("http://tizi.jingweikong.com")

my_list_of_links = r.html.links

my_list = []
my_list = list(my_list_of_links)

for item in my_list:
        if "http" in item:
            print(item)
