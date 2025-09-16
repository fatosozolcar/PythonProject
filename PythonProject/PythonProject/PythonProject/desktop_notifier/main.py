from plyer import notification
import time

if __name__ == '__main__':
    notification.notify(
        title="Başlık Girin:",
        message="açıklama girin",

        timeout=10

    )

    time.sleep(2)

