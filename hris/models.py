from django.db import models
from django.contrib.auth.models import User
from datetime import time
# Create your models here.



class Employee(models.Model):

    # PERSONAL INFORMATION 
    user = models.OneToOneField(User, null=True, blank=True,unique=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="Default_pfp.jpg", null=True, blank=True)
    employee_id = models.CharField(max_length=20,unique=True)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    employment_status = models.CharField(max_length=100, null=True, blank=True)
    name_ext = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    civil_status = models.CharField(max_length=20, blank=True, null=True)
    height_m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_type = models.CharField(max_length=10, blank=True, null=True)
    gsis_no = models.CharField(max_length=20, blank=True, null=True)
    pagibig_no = models.CharField(max_length=20, blank=True, null=True)
    philhealth_no = models.CharField(max_length=20, blank=True, null=True)
    sss_no = models.CharField(max_length=20, blank=True, null=True)
    tin_no = models.CharField(max_length=20, blank=True, null=True)
    agency_em = models.CharField(max_length=100, blank=True, null=True)
    citizenship = models.CharField(max_length=50, blank=True, null=True)

    # PERSONAL ADDRESS
    residential_house_no = models.CharField(max_length=10, blank=True, null=True)
    residential_street = models.CharField(max_length=100, blank=True, null=True)
    residential_subd = models.CharField(max_length=100, blank=True, null=True)
    residential_brgy = models.CharField(max_length=100, blank=True, null=True)
    residential_city = models.CharField(max_length=100, blank=True, null=True)
    residential_province = models.CharField(max_length=100, blank=True, null=True)
    residential_zipcode = models.CharField(max_length=10, blank=True, null=True)
    permanent_house_no = models.CharField(max_length=10, blank=True, null=True)
    permanent_street = models.CharField(max_length=100, blank=True, null=True)
    permanent_subd = models.CharField(max_length=100, blank=True, null=True)
    permanent_brgy = models.CharField(max_length=100, blank=True, null=True)
    permanent_city = models.CharField(max_length=100, blank=True, null=True)
    permanent_province = models.CharField(max_length=100, blank=True, null=True)
    permanent_zipcode = models.CharField(max_length=10, blank=True, null=True)

    #PERSONAL CONTACT
    telephone = models.CharField(max_length=20, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)

    # FAMILY BACKGROUND
    spouse_surname = models.CharField(max_length=100, blank=True, null=True)
    spouse_first_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_middle_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_name_ext = models.CharField(max_length=10, blank=True, null=True)
    spouse_occupation = models.CharField(max_length=100, blank=True, null=True)
    spouse_employer = models.CharField(max_length=100, blank=True, null=True)
    spouse_business_address = models.CharField(max_length=200, blank=True, null=True)
    spouse_telephone = models.CharField(max_length=20, blank=True, null=True)

    children1_name = models.CharField(max_length=100, blank=True, null=True)
    children1_BDAY = models.DateField(blank=True, null=True)

    children2_name = models.CharField(max_length=100, blank=True, null=True)
    children2_BDAY = models.DateField(blank=True, null=True)

    children3_name = models.CharField(max_length=100, blank=True, null=True)
    children3_BDAY = models.DateField(blank=True, null=True)

    children4_name = models.CharField(max_length=100, blank=True, null=True)
    children4_BDAY = models.DateField(blank=True, null=True)

    children5_name = models.CharField(max_length=100, blank=True, null=True)
    children5_BDAY = models.DateField(blank=True, null=True)

    children6_name = models.CharField(max_length=100, blank=True, null=True)
    children6_BDAY = models.DateField(blank=True, null=True)

    children7_name = models.CharField(max_length=100, blank=True, null=True)
    children7_BDAY = models.DateField(blank=True, null=True)

    children8_name = models.CharField(max_length=100, blank=True, null=True)
    children8_BDAY = models.DateField(blank=True, null=True)

    children9_name = models.CharField(max_length=100, blank=True, null=True)
    children9_BDAY = models.DateField(blank=True, null=True)

    children10_name = models.CharField(max_length=100, blank=True, null=True)
    children10_BDAY = models.DateField(blank=True, null=True)

    children11_name = models.CharField(max_length=100, blank=True, null=True)
    children11_BDAY = models.DateField(blank=True, null=True)

    children12_name = models.CharField(max_length=100, blank=True, null=True)
    children12_BDAY = models.DateField(blank=True, null=True)

    father_surname = models.CharField(max_length=100, blank=True, null=True)
    father_first_name = models.CharField(max_length=100, blank=True, null=True)
    father_middle_name = models.CharField(max_length=100, blank=True, null=True)
    father_name_ext = models.CharField(max_length=10, blank=True, null=True)
    mother_surname = models.CharField(max_length=100, blank=True, null=True)
    mother_first_name = models.CharField(max_length=100, blank=True, null=True)
    mother_middle_name = models.CharField(max_length=100, blank=True, null=True)


    # EDUCATIONAL PROGRAM

    # ELEMENTARY
    ELEMENTARY = models.CharField(max_length=200, blank=True, null=True)
    ELEMENTARY_BASIC_EDUCATION_DEGREE_COURSE = models.CharField(max_length=200, blank=True, null=True)
    ELEMENTARY_PERIOD_OF_ATTENDANCE_FROM = models.DateField(blank=True, null=True)
    ELEMENTARY_PERIOD_OF_ATTENDANCE_TO = models.DateField(blank=True, null=True)
    ELEMENTARY_HIGHEST_LEVEL_UNITS_EARNED = models.CharField(max_length=200, blank=True, null=True)
    ELEMENTARY_YEAR_GRADUATED = models.CharField(max_length=200, blank=True, null=True)
    ELEMENTARY_SCHOLARSHIP_ACADEMIC_HONORS_RECEIVED = models.CharField(max_length=200, blank=True, null=True)

    # SECONDARY
    SECONDARY = models.CharField(max_length=200, blank=True, null=True)
    SECONDARY_BASIC_EDUCATION_DEGREE_COURSE = models.CharField(max_length=200, blank=True, null=True)
    SECONDARY_PERIOD_OF_ATTENDANCE_FROM = models.DateField(blank=True, null=True)
    SECONDARY_PERIOD_OF_ATTENDANCE_TO = models.DateField(blank=True, null=True)
    SECONDARY_HIGHEST_LEVEL_UNITS_EARNED = models.CharField(max_length=200, blank=True, null=True)
    SECONDARY_YEAR_GRADUATED = models.CharField(max_length=200, blank=True, null=True)
    SECONDARY_SCHOLARSHIP_ACADEMIC_HONORS_RECEIVED = models.CharField(max_length=200, blank=True, null=True)


    # VOCATIONAL
    VOCATIONAL = models.CharField(max_length=200, blank=True, null=True)
    VOCATIONAL_BASIC_EDUCATION_DEGREE_COURSE = models.CharField(max_length=200, blank=True, null=True)
    VOCATIONAL_PERIOD_OF_ATTENDANCE_FROM = models.DateField(blank=True, null=True)
    VOCATIONAL_PERIOD_OF_ATTENDANCE_TO = models.DateField(blank=True, null=True)
    VOCATIONAL_HIGHEST_LEVEL_UNITS_EARNED = models.CharField(max_length=200, blank=True, null=True)
    VOCATIONAL_YEAR_GRADUATED = models.CharField(max_length=200, blank=True, null=True)
    VOCATIONAL_SCHOLARSHIP_ACADEMIC_HONORS_RECEIVED = models.CharField(max_length=200, blank=True, null=True)


    # COLLEGE
    COLLEGE = models.CharField(max_length=200, blank=True, null=True)
    COLLEGE_BASIC_EDUCATION_DEGREE_COURSE = models.CharField(max_length=200, blank=True, null=True)
    COLLEGE_PERIOD_OF_ATTENDANCE_FROM = models.DateField(blank=True, null=True)
    COLLEGE_PERIOD_OF_ATTENDANCE_TO = models.DateField(blank=True, null=True)
    COLLEGE_HIGHEST_LEVEL_UNITS_EARNED = models.CharField(max_length=200, blank=True, null=True)
    COLLEGE_YEAR_GRADUATED = models.CharField(max_length=200, blank=True, null=True)
    COLLEGE_SCHOLARSHIP_ACADEMIC_HONORS_RECEIVED = models.CharField(max_length=200, blank=True, null=True)

    # GRADUATE
    GRADUATE = models.CharField(max_length=200, blank=True, null=True)
    GRADUATE_BASIC_EDUCATION_DEGREE_COURSE = models.CharField(max_length=200, blank=True, null=True)
    GRADUATE_PERIOD_OF_ATTENDANCE_FROM = models.DateField(blank=True, null=True)
    GRADUATE_PERIOD_OF_ATTENDANCE_TO = models.DateField(blank=True, null=True)
    GRADUATE_HIGHEST_LEVEL_UNITS_EARNED = models.CharField(max_length=200, blank=True, null=True)
    GRADUATE_YEAR_GRADUATED = models.CharField(max_length=200, blank=True, null=True)
    GRADUATE_SCHOLARSHIP_ACADEMIC_HONORS_RECEIVED = models.CharField(max_length=200, blank=True, null=True)

    # DATE FILL UP
    DATE_OF_FILLUP = models.DateField(blank=True, null=True)




    employment_status = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)

    
    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.surname}"


class OfficialTime(models.Model):
    employee_id = models.CharField(max_length=20)
    day = models.CharField(max_length = 10)
    semester_id = models.CharField(max_length = 10, null= True, blank = True)
    official_office_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_office_out = models.TimeField(default='00:00:00', null=True, blank=True)
    official_honorarium_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_honorarium_time_out = models.TimeField(default='00:00:00', null=True, blank=True)
    official_servicecredit_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_servicecredit_time_out = models.TimeField(default='00:00:00', null=True, blank=True)
    official_overtime_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    official_overtime_time_out = models.TimeField(default='00:00:00', null=True, blank=True)


class AttendanceRecord(models.Model):
    employee_id = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    break_in = models.TimeField(default='00:00:00', null=True, blank=True)
    break_out = models.TimeField(default='00:00:00', null=True, blank=True)
    time_out = models.TimeField(default='00:00:00', null=True, blank=True)
    surplusHour_time_in = models.TimeField(default='00:00:00', null=True, blank=True)
    surplusHour_time_out = models.TimeField(default='00:00:00', null=True, blank=True)

    def __str__(self):
        return f"{self.employee_id} - {self.date}" if self.date else self.employee_id


class EditLogs(models.Model):
    attendance_record = models.ForeignKey(AttendanceRecord, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    logged_data = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)