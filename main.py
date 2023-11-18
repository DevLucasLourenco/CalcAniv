import locale
from datetime import timedelta, datetime

# traduzindo 
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# calculo tempo
suposta_data = datetime(2023, 12, 4).date()
meuNascimento = datetime(2002, 12, 3).date()

print(f'Nasci em {meuNascimento.strftime("%A, %d de %B de %Y")}')
print(f'Tenho {((suposta_data - meuNascimento)/365).days} anos')
