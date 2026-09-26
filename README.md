# Booking Class

A Python project that models travel bookings with classes, then uses them to analyze a sample set of hotel bookings.

## Why I built it

To apply OOP to data I understand well: travel bookings.

## What it is

I built a `Booking` class with reusable business logic that works for any type of booking, then expanded it with inheritance.

- **Classes and objects**: each booking is an object with its own guest, dates, route, price, provider and status.
- **Methods**: the business logic lives with the data it uses. Cancelling, calculating commission, lead time, duration, and days until the trip starts are written once and shared by every booking type.
- **Inheritance**: `HotelBooking` inherits everything from `Booking` and adds only what's specific to hotels: hotel name, room type, nights, price per night and its own commission rate.

```
Booking                    shared fields and business logic
└── HotelBooking           hotel fields, nights, price per night
```

The notebook (`analysis.ipynb`) loads 20 sample hotel bookings from a CSV into `HotelBooking` objects, then filters, sorts, sums, averages and groups them by provider, first in plain Python and then with pandas.

## Project files

```
booking-class/
├── booking.py      # Booking and HotelBooking classes
├── analysis.ipynb  # loading and analyzing the bookings
├── bookings.csv    # 20 sample hotel bookings
└── README.md

```

## Next steps

- Add `FlightBooking` and `CarRentalBooking` using the same `Booking` parent
- Add a rule-based `cancellation_risk()` method

