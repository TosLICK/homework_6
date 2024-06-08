import sys
import logging
import insert_
from connect import create_connection

functions = {
    "groups": insert_.insert_data_groups,
    "students": insert_.insert_data_students,
    "teachers": insert_.insert_data_teachers,
    "subjects": insert_.insert_data_subjects,
    "grades": insert_.insert_data_grades
}

def main(*args):
    try:
        with create_connection() as conn:
            if conn is not None:
                functions[sys.argv[1]](conn)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)

if __name__ == "__main__":
    main()