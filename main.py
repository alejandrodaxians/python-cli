import argparse
import logging

from properties import VACCINE_LIST
from models import QRCode, Vaccination, ValidationException
from qrlogic import generate_qr_code

def main_cli_logic():
    parser = argparse.ArgumentParser(description="Generate your vaccionation QR code.")
    parser.add_argument("-n", "--name", type=str, help="Your name", required=True)
    parser.add_argument("-b", "--birth", type=str, help="Your date of birth in YYYY-MM-DD format", required=True)
    parser.add_argument("-m", "--manufacturer", type=str, nargs="+", help="The vaccine manufacturer", required=True, choices = VACCINE_LIST)
    parser.add_argument("-d", "--date", type=str, nargs="+", help="The date of vaccination", required=True)
    args = parser.parse_args()

    if len(args.manufacturer) != len(args.date):
        logging.error("The number of vaccine manufacturer doesn't match with the number of vaccine dates.")
        exit(1)

    qr_code = QRCode(args.name, args.birth, [Vaccination(args.manufacturer[i], args.date[i]) for i in range(len(args.date))])
    generate_qr_code(qr_code)


if __name__ == "__main__":
    try:
        main_cli_logic()
    except ValidationException as e:
        logging.error(e)
    except Exception as e:
        logging.exception(e)