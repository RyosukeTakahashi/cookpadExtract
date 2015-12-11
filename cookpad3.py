import sqlite3
import sys
import urllib.request
# from bs4 import BeautifulSoup
import bs4

param = sys.argv
recipe_id = param[1]

# HTML を取得
html = urllib.request.urlopen("http://cookpad.com/recipe/" + recipe_id).read()

# スクレイピング用の BeautifulSoup オブジェクトを作成
temp = bs4.BeautifulSoup(html)
# brタグがあると、手順を取得する際、仕様上不都合があるので、置換しておく
temp_str = str(temp).replace("<br/>", "")

soup = bs4.BeautifulSoup(temp_str)

# レシピの材料部を取得
recipe_ingredients = soup.find("div", attrs={"id": "ingredients_list"})
# リンクが貼られている材料も取得しておく
ingredients_with_link = recipe_ingredients.findAll("a")

# レシピのタイトルを取得し、出力
recipe_title = soup.find("h1", attrs={"class": "recipe-title fn clearfix"})
print(recipe_title.string)

# 材料とその量を格納する配列を用意する
ingredient_names = []
ingredient_amounts = []

# 材料を取得
i = 0
for ingredient_name in recipe_ingredients.findAll("div", attrs={"class": "ingredient_name"}):
    ingredient_names.append(ingredient_name.string)

    # 材料名にリンクが付いていると、上記では取得できない（Noneとなる）。よって以下。
    if ingredient_name.string is None:
        ingredient_names[-1] = ingredients_with_link[i].string
        i += 1

# 材料の量を取得
for ingredient_amount in recipe_ingredients.findAll("div", attrs={"class": "ingredient_quantity amount"}):
    ingredient_amounts.append(ingredient_amount.string)


# 材料とその量を出力
print("")
i = 0
for i in range(len(ingredient_names)):
    print(ingredient_names[i], ingredient_amounts[i])

# 手順を取得して出力
print("")
steps = soup.find("div", attrs={"id": "steps"}).findAll("p", attrs={"class": "step_text"})
# print(steps)
i = 1

for step in steps:

    if isinstance(step, bs4.Tag):
        print(i, step.text)

    # print(i, step.string)
    i += 1



