from enum import Enum
from binarysearchTree import *

Menu = Enum('Menu', ['삽입', '삭제', '검색', '덤프', '키의범위', '종료'])

def select_Menu():
    '''메뉴선택'''
    s = ["({0}){1}".format(m.value, m.name) for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        

tree = BinarySearchTree()

while True:
    menu = select_Menu()

    if menu == Menu.삽입:
        key = int(input('삽입할 키를 입력 하세요 : '))
        val = input('삽입할 값을 입력하세요 : ')
        if not tree.add(key, val):
            print('삽입에 실패했습니다.')
    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력 하세요 : '))
        tree.remove(key)
    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력 하세요 : '))
        t = tree.search(key)
        if t is not None:
            print('이 키를 갖는 값은 {0}입니다'.format(t))
        else:
            print('해당하는 데이터가 없습니다.')
    elif menu == Menu.덤프:
        tree.dump()
    elif menu == Menu.키의범위:
        print('키의 최솟값은 {0}입니다'.format(tree.min_key()))
        print('키의 최댓값은 {0}입니다'.format(tree.max_key()))
    else:
        break