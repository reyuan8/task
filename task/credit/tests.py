import requests
from datetime import datetime
from credit.models import Borrower, CreditProgramm, BlockedTarget


BASE_URL = "https://stat.gov.kz/api/juridical/gov/?lang=ru"



def check_amount(programm_id: int, amount: int):
    programm = CreditProgramm.objects.filter(pk=programm_id).first()
    if programm is not None:
        if amount < programm.min_amount or amount > programm.max_amount:
            return {
                'message': 'Заявка не подходит по сумме'
            }
    return None


def check_age(programm_id: int, age: int):
    programm = CreditProgramm.objects.filter(pk=programm_id).first()
    if programm is not None:
        if age < programm.min_age or age > programm.max_age:
            return {
                'message': 'Заявка не подходит по возрасту'
            }
    return None


def check_target(target: str):
    api_url = BASE_URL + f"&bin={target}"
    r = requests.get(api_url)
    try:
        res = r.json()
        if res.get('success') == True:
            return {
                'message': 'иин является ИП'
            }
    except:
        return {
            'message': 'Connection error'
        }
    else:
        return None


def check_in_black_list(target: str):
    blocked_target = BlockedTarget.objects.filter(iin=target).first()
    if blocked_target is not None:
        return {
            'success': False,
            'message': 'Заемщик в черном списке'
        }


def create_borrower(target: str):
    day = target[4:6]
    month = target[2:4]
    year = target[0:2]
    if int(year) > 20:
        century = '19'
    else:
        century = '20'

    borrower, created = Borrower.objects.get_or_create(
        iin=target,
        birth_date = datetime.strptime(f"{century}{year}/{month}/{day}",'%Y/%m/%d')
    )

    return borrower
