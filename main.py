def url_maker(resort_id, app_id, key):
    base = "api.weatherunlocked.com/api/resortforecast/"
    resort_id = str(resort_id)
    app_id = str(app_id)
    key = str(key)

    url = base+resort_id+"?app_id="+app_id+"&app_key="+key
    return url


def setup_api():
    app_id = 87516043
    key = "82c84db08480af06fbe40d3a85190a0a"
    accept_header = "application/json"
    resort_id = 802019
    url = url_maker(resort_id, app_id, key)


def run():
    setup_api()
    # test


if __name__ == "__main__":
    run()
