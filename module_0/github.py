import numpy as np
number = np.random.randint(1,101)    # загадали число от 1 до 100

def game_core_v1(number):
    left = 1
    right = 100
    count = 0
    predict = np.random.randint(1,101)
    while number != predict:
        if number >= int((left + right)/2):
            left = int((left + right)/2)
            predict = np.random.randint(left,right + 1)
            count+=1
        else:
            right = int((left + right)/2)
            predict = np.random.randint(left,right)
            count+=1
    return(count)

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v1)