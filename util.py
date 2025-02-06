import datetime

def get_periods():
    return [
        (datetime.date(2023, 6, 26), datetime.date(2024, 6, 10), "kibor_22", 22.0),
        (datetime.date(2024, 6, 11), datetime.date(2024, 7, 29), "kibor_20_5", 20.5),
        (datetime.date(2024, 7, 30), datetime.date(2024, 9, 12), "kibor_19_5", 19.5),
        (datetime.date(2024, 9, 13), datetime.date(2024, 11, 4), "kibor_17_5", 17.5),
        (datetime.date(2024, 11, 5), datetime.date(2024, 12, 16), "kibor_15", 15.0),
        (datetime.date(2024, 12, 17), datetime.date(2025, 1, 27), "kibor_13", 13.0),
        (datetime.date(2025, 1, 28), datetime.date.today(), "kibor_12", 12.0),
    ]


def calculate_compensation_full_payment(full_payment_amount, full_payment_date, vehicle_delivery_date):
    date_after_60_days_fp = full_payment_date + datetime.timedelta(days=60)
    periods = get_periods()
    if vehicle_delivery_date <= date_after_60_days_fp:
        return -1

    total_compensation = 0
    current_date = date_after_60_days_fp

    for start_date, end_date, name, interest_rate in periods:
        if current_date > vehicle_delivery_date:
            break

        if end_date >= current_date:
            period_start = max(current_date, start_date)
            period_end = min(vehicle_delivery_date, end_date)
            days_in_period = (period_end - period_start).days + 1
            if days_in_period > 0:
                total_compensation += (full_payment_amount * (interest_rate + 3) / 100) * (days_in_period / 365)

            current_date = period_end + datetime.timedelta(days=1)

    return total_compensation