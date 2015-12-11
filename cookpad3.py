import sqlite3
import sys
import urllib.request
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

# レシピのタイトルを取得し、出力
recipe_title = soup.find("h1", attrs={"class": "recipe-title fn clearfix"})
print("レシピ名:"+recipe_title.string)


print("材料名:")
# レシピの材料部を取得
recipe_ingredients = soup.find("div", attrs={"id": "ingredients_list"})

for ingredient_name in recipe_ingredients.findAll("div", attrs={"class": "ingredient_name"}):
    if isinstance(ingredient_name, bs4.Tag):
        print(ingredient_name.text)

# 材料の量を取得
for ingredient_amount in recipe_ingredients.findAll("div", attrs={"class": "ingredient_quantity amount"}):
    if isinstance(ingredient_amount, bs4.Tag):
        print(ingredient_amount.text)

# 手順を取得して出力
print("")
steps = soup.find("div", attrs={"id": "steps"}).findAll("p", attrs={"class": "step_text"})
# print(steps)
i = 1

for step in steps:
    if isinstance(step, bs4.Tag):
        print(i, step.text)
    i += 1
