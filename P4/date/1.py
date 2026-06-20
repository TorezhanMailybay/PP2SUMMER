#Write a Python program to subtract five days from current date.
import datetime
x = datetime.datetime.now()

f = x - datetime.timedelta(days=5)
print(f)