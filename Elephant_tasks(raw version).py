# Project Name : Elephants Tasks
# Version = 17


import datetime


def task_name(numbers_type, total_number_of_units, total_number_of_completed_units):

    # Days
    now_day = datetime.datetime.today()
    start_day = datetime.datetime(2022, 3, 1)
    end_day = datetime.datetime(2022, 6, 10)
    number_of_days_left = (end_day - now_day).days + 1

    # 1 = المستقلة = individual
    if numbers_type == 1:
        
        number_of_units_completed = sum(total_number_of_completed_units)
        number_of_units_remaining = total_number_of_units - number_of_units_completed
        completion_rate = number_of_units_completed / total_number_of_units
        completion_rate_last_day = (number_of_units_completed - sum(total_number_of_completed_units[:-1])) / total_number_of_units
        completion_rate_last_week = (number_of_units_completed - sum(total_number_of_completed_units[:-7])) / total_number_of_units

    # 2 = التقدمية = progressive
    elif numbers_type == 2:

        number_of_units_completed = total_number_of_completed_units[-1]
        number_of_units_remaining = total_number_of_units - number_of_units_completed
        completion_rate = number_of_units_completed / total_number_of_units
        completion_rate_last_day = (number_of_units_completed - total_number_of_completed_units[-2]) / total_number_of_units
        completion_rate_last_week = (number_of_units_completed - sum(total_number_of_completed_units[:-7])) / total_number_of_units

    if number_of_days_left <= 0:
        print('You have passed the deadline \nModify at end_day')

    elif number_of_days_left > 0:

        daily_ration = number_of_units_remaining / number_of_days_left

        # Output Messages

        print('\n1 - Daily Ration : {:.4}'.format(daily_ration))
        print('\n2 - Number Of Days Left :', number_of_days_left)
        print('\n3 - Number Of Units Remaining :', number_of_units_remaining)
        print('\n4 - Number Of Units Completed :', number_of_units_completed)
        print('\n5 - Completion Rate : {:.2%} | Last Day : +{:.2%}\n|Last Week +{:.2%}'.format(completion_rate, completion_rate_last_day, completion_rate_last_week))
        print('\n6 - Number Of Past Days :', (now_day - start_day).days, '\n')


task_name(1, 229,
          [3, 2, 3, 2, 6, 2, 1, 13])


# task_name(2 , 313,[0 , 125 , 146 ])

