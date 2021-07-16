#!/usr/bin/env python3

from emailer import Emailer

from os import environ, stat
from os.path import exists, isfile, realpath
from time import sleep
from datetime import datetime
from argparse import ArgumentParser

def watch_canary(f):
  initial_file_access = stat(f).st_atime
  sleep(5)

  while True:
    file_access_time = stat(f).st_atime

    if file_access_time != initial_file_access:
      gmail_addr = environ["GMAIL_ADDR"]
      gmail_pass = environ["GMAIL_PASS"]

      with Emailer("smtp.gmail.com", 465) as email:
        # remove print stmts when running as cronjob or
        # scheduled task
        if email.authenticate(gmail_addr, gmail_pass):
          print("{*} Authentication successful")
        else:
          print("{-} Authentication unsuccessful")

        subject = "[WARNING] Canary Triggered"
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        message = f"[{now}] Someone accessed the canary file:\n\t {realpath(f)}"

        if email.send(gmail_addr, subject, message):
          print("{*} Successfully sent email")
        else:
          print("{-} Email could not be sent")
    break
  sleep(5)

if __name__ == "__main__":
  parser = ArgumentParser(description="Basic file canary script")
  parser.add_argument("FILE", help="File to act as canary")

  args = parser.parse_args()

  if exists(args.FILE) and isfile(args.FILE):
    watch_canary(args.FILE)
  else:
      print(f"{{-}} {args.FILE} does not exist")
