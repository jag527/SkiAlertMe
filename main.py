import urllib.request
import json


def get_file(url):
    # returns a file of a given url

    file = urllib.request.urlopen(url)
    return file


def date_convert(d):
    # takes in date with day-first style: '17/12/2021'
    # changes it to month-first style: '12/17/2021'

    day = d[:d.find("/")]
    month = d[d.find("/")+1:d.rfind("/")]
    year = d[d.rfind("/")+1:]
    return month + "/" + day + "/" + year


def file_to_json(f):
    # returns convertedDict js is a dictionary of the api call
    # js keys are ['id', 'name', 'country', 'continent', 'forecast']
    # js["name"] --> "Stratton Mountain"
    # js["forecast"][_] is a dictionary representing a 3 hour period
    #                   with important keys: date, snow_in.
    #                   key "mid" --> subkey "wx_desc" for weather descr.
    # js["forecast"][0] through js["forecast"][7] == day 1 (curr day)
    # js["forecast"][8] through js["forecast"][15] == day 1 (next day)

    d = f.read().decode('UTF-8')
    convertedDict = json.loads(d)
    return convertedDict


def parse_dict(js):
    # returns list of:
    # mountain, info about today, info about tomorrow, snow_rep link

    ans = [None] * 4
    ans[0] = js["name"]
    ans[3] = "https://www.stratton.com/the-mountain/mountain-report#/"

    # json info for current day
    day1 = ""
    total_snow1 = 0
    for x in range(8):
        dct = js["forecast"][x]
        day1 = date_convert(dct["date"])
        total_snow1 += dct["snow_in"]
        if x == 2:
            morn_weath1 = dct["mid"]["wx_desc"]
        if x == 4:
            mid_weath1 = dct["mid"]["wx_desc"]
        if x == 6:
            night_weath1 = dct["mid"]["wx_desc"]
    ans[1] = {"Day": day1, "Total Snowfall": round(total_snow1, 2),
              "Morning Weather": morn_weath1,
              "Midday Weather": mid_weath1,
              "Night Weather": night_weath1}

    # json info for next day
    day2 = ""
    total_snow2 = 0
    for x in range(8, 16):
        dct = js["forecast"][x]
        day2 = date_convert(dct["date"])
        total_snow2 += dct["snow_in"]
        if x == 10:
            morn_weath2 = dct["mid"]["wx_desc"]
        if x == 12:
            mid_weath2 = dct["mid"]["wx_desc"]
        if x == 14:
            night_weath2 = dct["mid"]["wx_desc"]
    ans[2] = {"Day": day2, "Total Snowfall": round(total_snow2, 2),
              "Morning Weather": morn_weath2,
              "Midday Weather": mid_weath2,
              "Night Weather": night_weath2}

    return ans


class SkiAlertMe:
    def __init__(self):
        # initializing object and API calls for Stratton Mountain

        self.app_id = 87516043
        self.key = "82c84db08480af06fbe40d3a85190a0a"
        self.accept_header = "application/json"
        self.resort_id = 802019

    def url_maker(self):
        # creates a url based on given class attributes

        base = "http://api.weatherunlocked.com/api/resortforecast/"
        resort_id = str(self.resort_id)
        app_id = str(self.app_id)
        key = str(self.key)
        num_days = "?num_of_days=2&"
        url = base+resort_id+num_days+"app_id="+app_id+"&app_key="+key
        return url


def run():
    alert = SkiAlertMe()
    url = alert.url_maker()
    file = get_file(url)
    js = file_to_json(file)
    parsed_lst = parse_dict(js)
    return parsed_lst


if __name__ == "__main__":
    run()
