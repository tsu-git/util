import pyinputplus as pyip
import sys

"""ask_preference_of_sandwich.py

    ユーザーにサンドイッチの好みを尋ねる。合計金額を表示する。
"""
total_amount = 0
total_title = '合計'

print("いらっしゃいませ！お好みのサンドイッチをおつくりします")
print()

# パンの種類：小麦パン、白パン、サワー種
menu_bread = {'小麦パン':120, '白パン':100, 'サワー種':150}
bread_list = [k for k in menu_bread.keys()]
response = pyip.inputMenu(bread_list, numbered=True)
total_amount += menu_bread[response]
print(f'  {response:10}{menu_bread[response]:7,}円')
print(f'  {total_title:10}{total_amount:7,}円')

# タンパク質の種類：チキン、ターキー、ハム、豆腐
menu_protein = {'チキン':120, 'ターキー':200, 'ハム':180, '豆腐':60}
protein_list = [k for k in menu_protein.keys()]
response = pyip.inputMenu(protein_list, numbered=True)
total_amount += menu_protein[response]
print(f'  {response:10}{menu_protein[response]:7}円')
print(f'  {total_title:10}{total_amount:7,}円')

# チーズが必要か
response = pyip.inputYesNo(prompt='チーズを入れますか？(yes/no) ')
if response == 'yes':
    # チーズの種類：チェダー、スイス、モッツアレラ
    menu_cheese = {'チェダー':140, 'スイス':170, 'モッツアレラ':180}
    cheese_list = [k for k in menu_cheese.keys()]
    response = pyip.inputMenu(cheese_list, numbered=True)
    total_amount += menu_cheese[response]
    print(f'  {response:10}{menu_cheese[response]:7}円')
    print(f'  {total_title:10}{total_amount:7,}円')

# マヨネーズ、からし、レタス、トマト
menu_sause_and_vegi = {'マヨネーズ':10, 'からし':10, 'レタス':50,
                       'トマト':70}
sause_and_vegi_list = [k for k in menu_sause_and_vegi.keys()]
response = pyip.inputMenu(sause_and_vegi_list, numbered=True)
total_amount += menu_sause_and_vegi[response]
print(f'  {response:10}{menu_sause_and_vegi[response]:7}円')
print(f'  {total_title:10}{total_amount:7,}円')

# TODO: サンドイッチがいくつ必要か。数字は1以上。
response = pyip.inputNum(prompt='このサンドイッチをいくつ作りますか？ ',
                         min=1, max=10)
total_amount += total_amount * response

# TODO: 合計金額表示する
print(f'  {total_title:10}{total_amount:7,}円')

sys.exit()
