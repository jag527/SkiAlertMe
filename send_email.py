import smtplib
import main


email_list = ["XXXXX@gmail.com",
              "XXXXX@gmail.com"]


def d_to_message(d):
    intro = "Report for " + d[0] + ": \n \n"
    day1 = "On " + str(d[1]["Day"]) + " there will be " + \
           str(d[1]["Total Snowfall"]) + " in. of total snowfall, with " + \
           d[1]["Morning Weather"].lower() + ", " +\
           d[1]["Midday Weather"].lower() + ", and " +\
           d[1]["Night Weather"].lower() + " " \
           + "weather throughout the day. \n \n"
    day2 = "On " + str(d[2]["Day"]) + " there will be " + \
           str(d[2]["Total Snowfall"]) + " in. of total snowfall, with " + \
           d[2]["Morning Weather"].lower() + ", " + \
           d[2]["Midday Weather"].lower() + ", and " +\
           d[2]["Night Weather"].lower() + " " + \
           "weather throughout the day. \n \n"
    conclude = "See more at " + d[3]
    message = "\n" + intro + day1 + day2 + conclude
    return message


def send_email(d, lst):
    # takes in a dictionary created in main.py
    # sends email with the info from the dictionary
    # sends emails to all addresses in lst

    server = smtplib.SMTP_SSL("smtp.gmail.com")
    server.login("XXXXX@gmail.com",
                 "xxxxx")
    message = d_to_message(d)

    for address in lst:
        server.sendmail("dailystrattonupdate@gmail.com",
                        address, message)

    server.quit()


def run():
    weather_dict = main.run()
    send_email(weather_dict, email_list)


if __name__ == "__main__":
    run()
