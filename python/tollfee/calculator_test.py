"""
Toll fee calculator
"""

import enum
import datetime

from vehicle import Car, Motorbike, Tractor, Emergency, Diplomat, Foreign, Military # Global import because of Python3. NOT usually recommended. Can be solved with a package (__init.py file).


class TollFreeVehicles(enum.Enum):
    Motorbike = 1
    Tractor = 2
    Emergency = 3
    Diplomat = 4
    Foreign = 5
    Military = 6


def get_toll_fee(vehicle, dates):
    """
    Calculate the total toll fee for one day

    Args:
        vehicle (vehicle.Vehicle): The vehicle.
        dates (list): Date and time (:py:class:`datetime.datetime`)
            of all passes on one day.

    Returns:
        int: The total toll fee for that day.
    """
    interval_start = dates[0]
    max_fee = 0
    total_fee = 0

    if _is_toll_free_vehicle(vehicle):
        return 0

    # This assumes that the list of datetimes is sorted by time
    for i in range(len(dates)):
        print('START', i)
        print("interval_start: ", interval_start)
        current_fee = toll_fee_passage(dates[i], vehicle)
        print("current_fee: ", current_fee)

        # Calculation of time intervall
        diff = dates[i] - interval_start
        minutes = diff.total_seconds() // 60
        print("minutes: ", minutes)

        if minutes <= 60: # Discuss < 60? Requirement: Only the highest fee should be charged for multiple passages within a 60 minute period.
            if current_fee > max_fee:
                total_fee -= max_fee
                total_fee += current_fee
                max_fee = current_fee
        else:
            total_fee += current_fee

            # Start new intervall
            interval_start = dates[i]
            max_fee = current_fee
        
        print("total_fee_end: ", total_fee)

    return min(total_fee, 60) # Requirement: The maximum fee for one day is 60 SEK


def toll_fee_passage(date, vehicle):
    """
    Return the fee for the passage at `date`.

    Args:
        date (datetime.datetime): The passage date.
        vehicle (vehicle.Vehicle): The vehicle.

    Returns:
        int: The toll fee for the passage
    """
    if _is_toll_free_date(date) or _is_toll_free_vehicle(vehicle):
        return 0

    hour = date.hour
    minute = date.minute

    # Requirement: Fees will differ between 9 SEK and 22 SEK, depending on the time of day.
    # If date-object is a proper datetime.datetime object we can remove some stuff to make it easier to understand
    if hour == 6 and minute <= 29:
        return 9
    elif hour == 6:
        return 16
    elif hour == 7:
        return 22
    elif hour == 8 and minute <= 29:
        return 16
    elif hour >= 8 and hour <= 14: # and minute <= 29: - It cost the hole hour, not just the first half hour
        return 9
    elif hour == 15 and minute <= 29:
        return 16
    elif hour == 15 or hour == 16:
        return 22
    elif hour == 17:
        return 16
    elif hour == 18 and minute <= 29:
        return 9
    else:
        return 0


def _is_toll_free_date(date):

    # Requirement: Fee-free days are; Saturdays, Sundays, ...
    if date.weekday() in (5, 6):
        return True
    # ...holidays and day before holidays and the whole month of July. See [Transportstyrelsen][] for details.
    # 2022 https://www.transportstyrelsen.se/sv/vagtrafik/Trangselskatt/Trangselskatt-i-goteborg/Tider-och-belopp-i-Goteborg/dagar-da-trangselskatt-inte-tas-ut-i-goteborg/
    # Utöver lördag och söndag samt juli månad, så är följande dagar befriade från trängselskatt under 2022:
    fee_free_days_2022 = [ 
                            datetime.date(2022, 1, 5), # 5-6 januari
                            datetime.date(2022, 1, 6),
                            datetime.date(2022, 4, 14), # 14-15 april
                            datetime.date(2022, 4, 15),
                            datetime.date(2022, 4, 18), # 18 april
                            datetime.date(2022, 5, 25), # 25-26 maj
                            datetime.date(2022, 5, 26),
                            datetime.date(2022, 6, 6), # 6 juni
                            datetime.date(2022, 6, 24), # 24 juni
                            datetime.date(2022, 11, 4), # 4 november
                            datetime.date(2022, 12, 26) # 26 december
                         ] # This list should be a constant in a config file or something like that.

    if date.date() in fee_free_days_2022:
        return True

    # I leave 2018 as it is. I don't like this. This should be configuration not code, because it changes every year.
    if date.year == 2018:
        if (date.month == 1 and (date.day == 1 or date.day == 5 or date.day == 6)
                or date.month == 3 and (date.day == 29 or date.day == 30)
                or date.month == 4 and (date.day == 2 or date.day == 30)
                or date.month == 5 and (date.day == 1 or date.day == 9 or date.day == 10)
                or date.month == 6 and (date.day == 5 or date.day == 6 or date.day == 22)
                or date.month == 7
                or date.month == 11 and date.day == 2
                or date.month == 12 and (date.day == 24 or date.day == 25 or date.day == 26 or date.day == 31)
            ):
            return True
        else:
            return False

    return False


def _is_toll_free_vehicle(vehicle): # Requirement: Some vehicle types are fee-free
    vehicle_type = vehicle.get_type()
    if vehicle == None:
        return False

    # return ( 
    #     vehicle_type == TollFreeVehicles.Motorbike.name or
    #     vehicle_type == TollFreeVehicles.Tractor.name or
    #     vehicle_type == TollFreeVehicles.Emergency.name or
    #     vehicle_type == TollFreeVehicles.Diplomat.name or
    #     vehicle_type == TollFreeVehicles.Foreign.name or
    #     vehicle_type == TollFreeVehicles.Military.name)
    
    return vehicle_type in TollFreeVehicles.__members__ # No changes if a new vehicle is added
