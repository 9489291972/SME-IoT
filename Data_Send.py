import random
import requests
import time


def send_random_data():
    url = "http://mangocity.appblocky.com/webdb/storeavalue.php?tag=curvol&value="

    while True:
        # Generate random current (between 0 and 10 Amps) and voltage (between 100 and 240 Volts)
        current = round(random.uniform(0, 10), 2)  # Random current between 0 and 10 Amps
        voltage = round(random.uniform(100, 240), 2)  # Random voltage between 100V and 240V

        # Prepare the value string to send
        value = f"current:{current},voltage:{voltage}"

        # Send the data to the server
        response = requests.get(url + value)

        if response.status_code == 200:
            print(f"Data sent successfully: {value}")
        else:
            print(f"Failed to send data. Status Code: {response.status_code}")

        # Wait for 10 seconds before sending the next value
        time.sleep(10)


if __name__ == "__main__":
    send_random_data()
