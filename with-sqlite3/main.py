from funcs_for_sqlphonebook import get_status_code, work_with_db


def start():
    code = get_status_code()
    work_with_db(code)


start()





