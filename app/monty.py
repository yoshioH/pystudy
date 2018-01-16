# -*- coding: utf-8 -*-
import random

def get_random_num() -> int:
    '''
    このスクリプトでのみ通用する乱数を生成する
    '''
    return random.randrange(3)

def other_random_num(*args:int) -> int:
    '''
    引数と一致しない乱数を取得する
    '''
    candidate_num = 0
    while candidate_num in args:
        candidate_num = get_random_num()

    return candidate_num    

def win_door() -> int:
    '''
    正解のドア
    '''
    return get_random_num()

def host_hint(win_num:int, guest_num:int) -> int:
    '''
    ホストのヒント
    '''
    if win_num == guest_num:
        return other_random_num(win_num)

    return other_random_num(win_num, guest_num)

def the_game(will_change:bool) -> bool:
    '''
    ゲームを実施する.勝った場合はTRUE
    '''
    # 正解ドアを設定
    win_num = win_door()

    # ゲストが開くドアを選択（1回目）
    guest_num = get_random_num()

    # ホストがヒント
    host_num = host_hint(win_num, guest_num)

    # ゲストが開くドアを選択（2回目）
    if will_change:
        guest_num = other_random_num(host_num, guest_num)

    # 答え合わせ
    return win_num == guest_num

will_change = True
win_count = 0
for i in range(90000):
    if the_game(will_change):
        win_count += 1

print (win_count)



