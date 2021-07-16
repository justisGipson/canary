### CANARY

Simple scripts that act as the `canary in the coal mine` to alert via email whenever a specific file it accessed.

#### Usage

Following environment variable need to be set:
	- `EMAIL_ADDR`: your gmail address
	- `EMAIL_PASS`: your gmail password

NOTE: If you are using 2FA you need to create an [app password](https://www.lifewire.com/get-a-password-to-access-gmail-by-pop-imap-2-1171882)

```
usage: canary.py [-h] FILE

Basic file canary Python program

positional arguments:
  FILE        File to act as canary

optional arguments:
  -h, --help  show this help message and exit
```

#### Example

`python3 canary.py secret.txt`
