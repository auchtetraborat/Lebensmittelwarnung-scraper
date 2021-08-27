from Lebensmittelwarnung import WarningFeedUrl, WarningFeed

type = "alle"
region = "alle_bundeslaender"

url = WarningFeedUrl.create(type,region)
feed = WarningFeed(url)
js = feed.export_to_json()
print(js)