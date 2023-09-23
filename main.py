import eel
from GoogleNews import GoogleNews
import pyshorteners

@eel.expose
def get_actual_news(country, language):
    google_news = GoogleNews(period='5d', lang=language.split(' - ')[-1])
    google_news.search(country.lower())
    result = google_news.result()

    news_dict = {}

    for item in result:
        news_item = {
            "Title": item["title"],
            "Date/Time": item["date"],
            "Description": item["desc"],
            "Link": item["link"]
        }

        if item["title"] not in news_dict:
            news_dict[item["title"]] = news_item

    news_list = list(news_dict.values())


    news_html = "<ul style='margin-left: -40px;'>"
    for news_item in news_list:
        news_html += f"<hr><h4 style='color: black;text-weight: bold;;'>{news_item['Title']}</h4>"
        news_html += f"Date/Time: {news_item['Date/Time']}<br>"
        news_html += f"Description: {news_item['Description']}<br>"
        news_html += f"Link: <a target='_blank' href=\"{news_item['Link']}\">{pyshorteners.Shortener().tinyurl.short(news_item['Link'])}</a><hr><br><br>"

    news_html += "</ul>"

    return news_html


eel.init('web')
eel.start('main.html', size=(535, 600))