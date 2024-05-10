import requests
from datetime import datetime
import smtplib
import time
MY_EMAIL = "your_email_adress"
MY_PASSWORD = "password_to_email_adress"

MY_LAT = 
MY_LONG = 

def is_close():


    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 < iss_latitude < MY_LAT+5 and  MY_LONG-5 < iss_longitude < MY_LONG+5:
      return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour > sunset and time_now.hour < sunrise:
        return True



while True:
    time.sleep(60)
    if is_night() and is_close():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="youremail@adress.com",
                msg=f"Look Up!\n\nLook Up! The ISS is close,you can easy spot him",
            )








