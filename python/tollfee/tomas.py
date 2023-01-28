import datetime
from calculator import *

# Test data
my_car = Car()
my_motorbike = Motorbike() 
my_tractor = Tractor() 
my_emergency = Emergency() 
my_diplomat = Diplomat() 
my_foreign = Foreign() 
my_military = Military()

# Dates
my_datetime0 = datetime.datetime(2022, 9, 5, 5, 5, 00)
my_datetime1 = datetime.datetime(2022, 1, 7, 6, 5, 00)
my_datetime2 = datetime.datetime(2022, 1, 7, 6, 45, 00)
my_datetime3 = datetime.datetime(2022, 1, 7, 7, 6, 00)
my_datetime4 = datetime.datetime(2022, 1, 7, 8, 5, 00)
my_datetime5 = datetime.datetime(2022, 1, 7, 8, 35, 00)
my_datetime6 = datetime.datetime(2022, 1, 7, 9, 5, 00)
my_datetime7 = datetime.datetime(2022, 1, 7, 13, 5, 00)
my_datetime8 = datetime.datetime(2022, 1, 7, 14, 5, 00)
my_datetime9 = datetime.datetime(2022, 1, 7, 15, 5, 00)
my_datetime10 = datetime.datetime(2022, 1, 7, 15, 45, 00)
my_datetime11 = datetime.datetime(2022, 1, 7, 16, 5, 00)
my_datetime12 = datetime.datetime(2022, 1, 7, 17, 5, 00)
my_datetime13 = datetime.datetime(2022, 1, 7, 18, 5, 00)
my_datetime14 = datetime.datetime(2022, 1, 7, 18, 35, 00)
my_datetime15 = datetime.datetime(2022, 1, 7, 19, 35, 00)

#print(get_toll_fee(my_car, [my_datetime1, my_datetime3]))
#print(get_toll_fee(my_car, [my_datetime1, my_datetime2, my_datetime3]))
#print(get_toll_fee(my_car, [my_datetime1, my_datetime2, my_datetime3, my_datetime4]))

# Test max fee
print(get_toll_fee(my_car, [my_datetime1, my_datetime2, my_datetime3, my_datetime4, my_datetime5, my_datetime6, my_datetime7, my_datetime8, my_datetime9, my_datetime10]))
#print(toll_fee_passage(my_datetime1, my_car))

