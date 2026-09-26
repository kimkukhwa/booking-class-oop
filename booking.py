from datetime import date


class Booking:
    commission_rate = 0.05
    booking_count = 0

    def __init__(
        self,
        booking_id,
        guest_name,
        booking_date,
        start_date,
        end_date,
        depart_country,
        destination_country,
        price,
        provider=None,
        status="confirmed",
        commission_rate=None,
    ):
        self.booking_id = booking_id
        self.guest_name = guest_name
        self.booking_date = booking_date
        self.start_date = start_date
        self.end_date = end_date
        self.depart_country = depart_country
        self.destination_country = destination_country
        self.price = price
        self.provider = provider
        self.status = status
        if commission_rate is not None:
            self.commission_rate = commission_rate
        Booking.booking_count += 1

    def __repr__(self):
        return (
            f"{type(self).__name__}(booking_id={self.booking_id!r}, "
            f"guest_name={self.guest_name!r}, "
            f"price={self.price!r}, "
            f"status={self.status!r})"
        )

    def duration_days(self):
        return (self.end_date - self.start_date).days

    def cancel(self):
        if self.status != "cancelled":
            self.status = "cancelled"
            return f"Booking {self.booking_id} has been cancelled."
        return "Booking is already cancelled."

    def commission(self):
        if self.status != "cancelled":
            return round(self.price * self.commission_rate, 2)
        return 0.0

    def lead_time(self):
        return (self.start_date - self.booking_date).days

    def days_until_start(self):
        return (self.start_date - date.today()).days


class HotelBooking(Booking):
    commission_rate = 0.111

    def __init__(self, hotel_name, room_type=None, **kwargs):
        super().__init__(**kwargs)
        self.hotel_name = hotel_name
        self.room_type = room_type

    @classmethod
    def from_dict(cls, data):
        rate = data.get("commission_rate")
        return cls(
            hotel_name=data["hotel_name"],
            room_type=data.get("room_type"),
            booking_id=int(data["booking_id"]),
            guest_name=data["guest_name"],
            booking_date=date.fromisoformat(data["booking_date"]),
            start_date=date.fromisoformat(data["start_date"]),
            end_date=date.fromisoformat(data["end_date"]),
            depart_country=data["depart_country"],
            destination_country=data["destination_country"],
            price=float(data["price"]),
            provider=data.get("provider"),
            status=data.get("status") or "confirmed",
            commission_rate=float(rate) if rate else None,
        )

    def __repr__(self):
        return (
            f"{type(self).__name__}(booking_id={self.booking_id!r}, "
            f"guest_name={self.guest_name!r}, "
            f"hotel_name={self.hotel_name!r}, "
            f"price={self.price!r}, "
            f"status={self.status!r})"
        )

    def nights(self):
        return self.duration_days()

    def price_per_night(self):
        nights = self.nights()
        if nights == 0:
            return self.price
        return round(self.price / nights, 2)


if __name__ == "__main__":
    hotel = HotelBooking(
        booking_id=1001,
        guest_name="KukHwa Kim",
        hotel_name="Grand Palace Hotel",
        booking_date=date(2026, 9, 1),
        start_date=date(2026, 10, 15),
        end_date=date(2026, 10, 25),
        depart_country="Canada",
        destination_country="Spain",
        price=1250.00,
    )

    print(hotel)
    print("Nights:", hotel.nights())
    print("Per night:", hotel.price_per_night())
    print("Commission:", hotel.commission())
    print("booking count: ", Booking.booking_count)
