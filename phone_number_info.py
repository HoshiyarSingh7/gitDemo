


# install phonenumbers module

[12:54, 2/25/2022] Hoshiyar: import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input('Enter no. with +91:')
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(car)
print(reg)