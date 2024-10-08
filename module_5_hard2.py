import time

"""
не понятно как рабоать с хещированными данными. Тут должен быть хещ-пароль"
                остальное работает
"""


class User:
    users = []

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        User.users.append(self)

    def __repr__(self):
        return (f'{self.nickname} : {self.password} - {self.age} лет')

    # def __hash__(self):
    #     return hash(self.password)


class Video:
    videos = []

    def __init__(self, title, duration, adult_mode=False, time_now=0):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now

    def __repr__(self):
        return (f'{self.title} - {self.duration} секунд')


class UrTube:
    def __init__(self, current_user=None):
        self.users = User.users
        self.videos = Video.videos
        self.current_user = None

    def register(self, nickname, password, age):
        users_list = []
        for i in User.users:
            users_list.append(i.nickname)
        if nickname in users_list:
            print(f'Пользователь с ником {nickname} уже существует')
        if nickname not in users_list:
            User(nickname, password, age)
            self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for i in User.users:
            if nickname == i.nickname and password == i.password:
                self.current_user = nickname
                # print('You are in')
            if nickname == i.nickname and password != i.password:
                print('WRONG PASSWORD')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        return Video.videos.extend(args)

    def get_videos(self, word):
        search_list = []
        for each_video in Video.videos:
            b = each_video.title
            if word.lower() in b.lower():
                search_list.append(b)
        return search_list

    def watch_video(self, movie_name):
        pass

    def watch_video(self, movie_name):
        for each_movie in Video.videos:

            if each_movie.title == movie_name and each_movie.adult_mode == False:
                self.time_goes(each_movie.duration)

            if each_movie.title == movie_name and each_movie.adult_mode == True:
                for i in User.users:
                    if i.nickname == self.current_user:
                        if i.age >= 18:
                            # print(f'{i.nickname} Ur in')
                            UrTube.time_now = each_movie.duration
                            self.time_goes(UrTube.time_now)
                            break
                        if i.age < 18:
                            print('Вам нет 18 лет, пожалуйста, покиньте страницу')

        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')

    @staticmethod
    def time_goes(rang):
        for i in range(rang):
            time.sleep(1)
            print(i + 1, end=' ')
        time.sleep(1)
        print('конец видео"')
        return UrTube.time_now == 0


# Код для проверки:

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
