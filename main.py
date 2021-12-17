import urllib.request


class SkiAlertMe:
    def __init__(self):
        self.app_id = 87516043
        self.key = "82c84db08480af06fbe40d3a85190a0a"
        self.accept_header = "application/json"
        self.resort_id = 802019  # Stratton

    def url_maker(self):
        base = "http://api.weatherunlocked.com/api/resortforecast/"
        resort_id = str(self.resort_id)
        app_id = str(self.app_id)
        key = str(self.key)
        url = base+resort_id+"?app_id="+app_id+"&app_key="+key
        return url

    def read_file(self, url):
        f = urllib.request.urlopen(url)
        print(f.read())

        return url


def run():
    alert = SkiAlertMe()
    url = alert.url_maker()
    alert.read_file(url)


if __name__ == "__main__":
    run()
