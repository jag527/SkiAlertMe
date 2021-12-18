import smtplib
import main


def d_to_message(d):
    intro = "Report for " + d[0] + ": \n"
    day1 = "On " + str(d[1]["Day"]) + " there will be " + \
           str(d[1]["Total Snowfall"]) + " in. of total snowfall, with " + \
           d[1]["Morning Weather"].lower() + ", " +\
           d[1]["Midday Weather"].lower() + ", and " +\
           d[1]["Night Weather"].lower() + " " \
           + "weather throughout the day. \n"
    day2 = "On " + str(d[2]["Day"]) + " there will be " + \
           str(d[2]["Total Snowfall"]) + " in. of total snowfall, with " + \
           d[2]["Morning Weather"].lower() + ", " + \
           d[2]["Midday Weather"].lower() + ", and " +\
           d[2]["Night Weather"].lower() + " " + \
           "weather throughout the day. \n"
    conclude = "See more at " + d[3]
    return intro + day1 + day2 + conclude


def send_email(d=""):
    # takes in a dictionary created in main.py
    # sends email with the info from the dictionary

    server = smtplib.SMTP_SSL("smtp.gmail.com")
    server.login("XXXX@gmail.com",
                 "XXXXX")
    message = d_to_message(d)
    print(message)
    server.sendmail("dailystrattonupdate@gmail.com",
                    "jgrossman1919@yahoo.com",
                    message)
    server.quit()


def run():
    d = main.run()
    send_email(d)


if __name__ == "__main__":
    run()
