import os
from datetime import date
from time import sleep

from data_base_tools.database_tools import DataBaseTools

path = os.getcwd()
print(path)
container = []
counter = 0
while True:
    for _, _, file_names in os.walk("test_folder1" or
                                    "test_folder"):
        for file_name in file_names:
            if file_name not in container:
                container.append(file_name)
                for plate_name in container:
                    plate_size = plate_name.split("_")[0]
                    qty = plate_name.split("_")[1]
                    company_name = plate_name.split("_")[2]
                    file_name = "_".join(plate_name.split("_")[3:])
                    if path == r'D:\NEW_WORKFOLDER\_telegramm_bot_folder_parser_worked':
                        equipment = 'BLUE'

                    add_date_time = date.today()
                    punch = 'NULL'
                    stage = 'NULL'
                    operator = 'NULL'
                    ready_datetime = 'NULL'

                    DataBaseTools().insert_plate_info_in_table(company_name,
                                                               qty,
                                                               file_name,
                                                               plate_size,
                                                               equipment,
                                                               add_date_time,
                                                               punch,
                                                               stage,
                                                               operator,
                                                               ready_datetime)

                    print(f"{counter} {plate_size} {qty} {company_name} {file_name} {equipment} {add_date_time}")
                    counter += 1
                    sleep(0.01)
