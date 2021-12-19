time = int(input('duration'))
h, m, s = time // 3600, time // 60 % 60, time % 60
print(f'{h} час {m} мин {s} cек')