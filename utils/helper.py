from datetime import date
from datetime import datetime

################# FUNÇÕES ################
def date_para_str(data: date) -> str:
    return datetime.strftime('%d/%m/%Y')

def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')

def moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'

