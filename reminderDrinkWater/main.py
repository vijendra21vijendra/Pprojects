import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="please drink water now",
            message="very necessary",
            app_icon="./iconfile.ico",
            timeout=2
        )
        # time.sleep(60*60) # i can set 60*60
        time.sleep(3*3)
        # to run in background do
        # pythonw main.py
        # to kill go in task manager and kil it named python
