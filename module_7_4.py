# Пример входных данных
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print()

# Использование format():
print('Команда Волшебники Данных решила задач: {}!'.format(score_2))
print('Волшебники Данных решили задачи за {} с'.format(team2_time))
print()

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total}, в среднем по {time_avg} секунды на задачу!')
print()


################# КОНЕЦ ЗАДАНИЯ #########################################


'''Далее баловство, можно не смотреть. Просто попытка создать таблицу по результатам.'''

print('-' * 57)
print('-' * 57)
team1 = 'Мастера кода'
team2 = 'Волшебники данных'
print(f'\033[31m\033[1m{team1:>30}\033[0m\t|\t\033[34m\033[1m{team2}\033[0m\t|')
print('-' * 57)
print(f'\033[32mКол_во игроков:\033[0m {team1_num:>15}\t|\t{team2_num:>15}\t\t|')
print('-' * 57)
print(f'\033[32mРешено задач:\033[0m {score_1:>17}\t|\t{score_2:>15}\t\t|')
print('-' * 57)
print(f'\033[32mВремя решения:\033[0m {team1_time:>16}\t|\t{team2_time:>15}\t\t|')
print('-' * 57)
av_time1 = round(team1_time / score_1, 2)
av_time2 = round(team2_time / score_2, 2)

print(f'\033[32mСреднее время:\033[0m {av_time1:>16}\t|\t{av_time2:>15}\t\t|')
print('-' * 57)

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды \033[34m\033[1mВолшебники Данных\033[0m!'
else:
    result = 'Ничья!'
print(result)

print('\033[47m   белый     \033[0m')  # не совсем белый фон какой-то
print('\033[44m   синий     \033[0m')
print('\033[41m   красный   \033[0m')
