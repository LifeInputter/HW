team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
team1_name = '"Мастера кода"'
team2_name = '"Волшебники данных"'

# Использование %:
print("В команде %s участников: %s" % (team1_name, team1_num))
print("В команде %s участников: %s" % (team2_name, team2_num))
if team1_num > 0 and team2_num > 0:
    result = print("Итого сегодня в командах участников: %s и %s" % (team1_num, team2_num))
elif team1_num == team2_num:
    result = print("Итого сегодня в командах участников поровну: %s и %s" % (team1_num, team2_num))
else:
    result = print("Соревновнания отменены")

# Использование format():

print("Количество задач, решенных командой {} - {}; {} - {}.".format(team1_name, score1, team2_name, score2))
print("Время, за которое команда {} решила задачи - {:.1f}. Время, за которое команда {} решила задачи - {:.1f}."
      .format(team2_name, team2_time, team1_name, team1_time))

# Использование f-строк:
print(f"Количество решенных задач по командам: {team1_name} - {score1}; {team2_name} - {score2}")
if score1 or score2 > 0:
    result = print(f'Команды решили {score1}  и {score2} задач. Общее количество решенных задач - {score1 + score2}.')
else:
    print("Решено задач 0")

rounded = round((team1_time + team2_time) / (score1 + score2), 2)
print(f"Среднее время решения задачи = {rounded} сек.")

print(f"{"Исход соревнования:".upper():*^30}")
if score1 > score2 or score1 == score2 and team1_time < team2_time:
    result = print(f"Победа команды {team1_name}")
elif score1 < score2 or score1 == score2 and team1_time > team2_time:
    result = print(f"Победа команды {team2_name}")
else:
    result = print("Ничья")
