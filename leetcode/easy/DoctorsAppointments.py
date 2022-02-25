import unittest

"""

Problem

We want to build a simple in-memory scheduling system for booking appointments with doctors

Facts

 - There is a fixed list of doctors  ["d1", "d2", "d3"] represented as strings
 - Every doctor works every day from [9 to 17] hours
 - Appointments are always 1 hour long on the hour


Guidelines

 - Stick to the functionality specified, keep it simple


Implement the schedule's data structure and the following functionality:
"""
doctors = ["d1", "d2", "d3"]
doctors_dict = dict()

class DoctorsAppointment:
    def __init__(self, doctor, appointment):
        apt_date = doctors_dict[doctor][appointment.date]
        for i in range(len(apt_date)):
            if apt_date[i].timeslot == appointment.timeslot:
                apt_date[i] = appointment



class Appointment:
    def __init__(self, date, timeslot, doctor, patient, isBooked):
        self.date = date
        self.timeslot = timeslot if 9 <= timeslot <= 17 else -1
        self.doctor = doctor
        self.patient = patient
        self.isBooked = isBooked


def populatedict():
    for d in doctors:
        if d not in doctors_dict:
            #at the end, the range function returns the total of days available, so that you can book 365 days of the year, however, I just chose 7, but it can be modified to something bigger
            days_in_year_dict = {day:[Appointment(day, n + 8, d, None, False) for index, n in enumerate(range(1, 8))] for day in range(7)}
            doctors_dict[d] = days_in_year_dict


def printdictcontents():
    for doctor in doctors_dict.keys():
        for day in doctors_dict[doctor]:
            for apt in doctors_dict[doctor][day]:
                print(f"Appointment for Doctor:{doctor} on day:{day} with details date:{apt.date}, timeslot:{apt.timeslot}, doctor:{apt.doctor}, patient:{apt.patient}, isBooked:{apt.isBooked}")


def isDoctorAvailable(doctor, new_appointment):
    for appointment in doctors_dict[doctor][new_appointment.date]:
        if appointment.date == new_appointment.date and appointment.timeslot == new_appointment.timeslot and appointment.patient is None and appointment.isBooked is False:
            return True

    return False


def get_appointments(date: int):
    """
    Returns a list containing every appointment created for a date
    each appointment contains the doctor, the patient, and the timeslot
    """
    appointments_based_on_dates = []
    for doctor in doctors_dict.keys():
        for day in doctors_dict[doctor]:
            for apt in doctors_dict[doctor][day]:
                if apt.date == date and apt.isBooked:
                    appointments_based_on_dates.append([doctor, apt.patient, apt.timeslot])

    return appointments_based_on_dates


def get_availability(date: int):
    """
    Returns a list containing the appointment slots that have NOT been booked on a date.
    Each AvailableSlot contains the doctor, and the available timeslot.
    """
    availability_based_on_dates = []
    for doctor in doctors_dict.keys():
        for day in doctors_dict[doctor]:
            for apt in doctors_dict[doctor][day]:
                if apt.isBooked is False and apt.date == date:
                    availability_based_on_dates.append([doctor, apt.timeslot])

    return availability_based_on_dates


def create_appointment(
        date: int,
        timeslot: int,
        doctor: str,
        patient: str
):
    """
    Returns False if doctor invalid, already booked, etc.
    Returns True if the appointment was added.
    """
    apt = Appointment(date, timeslot, doctor, patient, True)

    if doctor not in doctors:
        return False
    elif isDoctorAvailable(doctor, apt):
        DoctorsAppointment(doctor, apt)
        return True

    return False


class Solution(unittest.TestCase):

    def test_addAppointment(self):
        doctors_dict.clear()
        populatedict()
        self.assertEqual(create_appointment(0, 9, "d1", "p1"), True)

    def test_addRepeatedAppointment(self):
        doctors_dict.clear()
        populatedict()
        create_appointment(0, 9, "d1", "p1")
        self.assertEqual(create_appointment(0, 9, "d1", "p1"), False)

    def test_get_appointments(self):
        doctors_dict.clear()
        populatedict()
        create_appointment(1, 9, "d1", "p1")
        create_appointment(1, 10, "d2", "p2")
        create_appointment(1, 11, "d3", "p3")
        create_appointment(2, 12, "d1", "p5")
        create_appointment(2, 13, "d2", "p6")
        create_appointment(2, 14, "d3", "p7")
        create_appointment(3, 12, "d1", "p5")
        create_appointment(3, 13, "d2", "p6")
        create_appointment(3, 14, "d3", "p7")
        self.assertEqual(get_appointments(2), [['d1', 'p5', 12], ['d2', 'p6', 13], ['d3', 'p7', 14]])

    def test_get_availability(self):
        doctors_dict.clear()
        populatedict()
        for i in range(1, 3):
            for doc in doctors:
                create_appointment(0, i+8, doc, "p1")

        expected_result = [['d1', 11], ['d1', 12], ['d1', 13], ['d1', 14], ['d1', 15], ['d2', 11], ['d2', 12], ['d2', 13], ['d2', 14], ['d2', 15], ['d3', 11], ['d3', 12], ['d3', 13], ['d3', 14], ['d3', 15]]
        self.assertEqual(get_availability(0), expected_result)


if __name__ == '__main__':
    unittest.main()
