import argparse
import logging
from datetime import datetime, timedelta
import pytz
from time import sleep

def main(booking_hour):
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    time_zone = pytz.timezone('Europe/Madrid')
    time_now = datetime.now(time_zone)
    start_time = datetime.strptime(str(booking_hour), '%H%M')

    while(1):
        logging.info(f"Waiting booking hour {start_time}")
        if (time_now.minute == start_time.minute) & (time_now.hour == start_time.hour):
            logging.info(f"Hora es: {datetime.now()} UTC / {time_now} Europa")
            break
        
        sleep_h = start_time.hour - time_now.hour
        sleep_m = start_time.minute - time_now.minute
        if (sleep_h*60 + sleep_m) >= 2:
            sleep((sleep_h*60 + sleep_m - 1)*60)
        elif (sleep_h*60 + sleep_m) < 2 & (sleep_h*60 + sleep_m) >= 1:
            sleep(20)
        else:
            sleep(1)
        time_now = datetime.now(time_zone)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CLI tool to book classes on AimHarder"
    )
    parser.add_argument("--booking-hour", required=True, type=int, help="Booking hour")

    args = parser.parse_args()
    input = {key: value for key, value in args.__dict__.items() if value is not None}
    main(**input)