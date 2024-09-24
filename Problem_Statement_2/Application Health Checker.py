import requests
import time

url = 'http://udemy.com'
interval = 10  # in seconds

def check_application_health():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Application is UP (HTTP {response.status_code})")
        else:
            print(f"Application is DOWN (HTTP {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN (Exception: {e})")

if __name__ == "__main__":
    while True:
        check_application_health()
        time.sleep(interval)