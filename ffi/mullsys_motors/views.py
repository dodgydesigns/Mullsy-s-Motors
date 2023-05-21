import csv
import datetime
from django.shortcuts import render

from mullsys_motors.models import Rental


def read_data():
    """Read in all the MOCK_DATA entries, create Rental objects from each and save in DB."""
    Rental.objects.all().delete()  # For the testers so they don't double up each run.
    with open("mullsys_motors/MOCK_DATA.csv", newline="\r\n") as csv_file:  # Hard coded because easier
        mock_data_reader = csv.reader(csv_file)
        for row in mock_data_reader:
            try:
                if row[0] == "id":
                    continue
                formatted_date = datetime.datetime.strptime(row[7], "%m/%d/%Y").date()
                rental = Rental(
                    rental_id=row[0],
                    customer_first_name=row[1],
                    customer_last_name=row[2],
                    customer_email=row[3],
                    vehicle_vin=row[4],
                    vehicle_make=row[5],
                    vehicle_model=row[6],
                    rental_start_date=formatted_date,
                    rental_duration=row[8],
                    rental_day_rate=row[9],
                    paid="They're Paid up" if row[10] == "paid" else "Chase Them Down!",
                )
                rental.save()

            except Exception as e:
                # log exception
                continue


def initial(request):
    """ """
    read_data()
    all_rentals = Rental.objects.all()
    context = {
        "rentals_list": list(all_rentals.values()),
    }
    return render(request, "mullsys_motors/index.html", context)


def all(request):
    """ """
    all_rentals = Rental.objects.all()
    context = {
        "rentals_list": list(all_rentals.values()),
    }
    return render(request, "mullsys_motors/index.html", context)


def delinquents(request):
    """ """
    delinquent_rentals = Rental.objects.filter(paid="Chase Them Down!")
    context = {
        "rentals_list": list(delinquent_rentals.values()),
    }
    return render(request, "mullsys_motors/index.html", context)
