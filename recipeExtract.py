import sys
import urllib.request
import bs4



recipe_id = input("input recipe id:")

# HTML を取得し、bs4で読み取れるようにする
html = urllib.request.urlopen("https://cookpad.com/recipe/" + recipe_id).read()
soup = bs4.BeautifulSoup(html)

# レシピのタイトルを取得し、出力
recipe_title = soup.find("h1", attrs={"class": "recipe-title fn clearfix"})
print("レシピ名:"+recipe_title.string)

# レシピの材料部を取得
recipe_ingredients = soup.find("div", attrs={"id": "ingredients_list"})
ingredient_names = recipe_ingredients.findAll("div", attrs={"class": "ingredient_name"})
ingredient_amounts = recipe_ingredients.findAll("div", attrs={"class": "ingredient_quantity amount"})

# 材料：量 を出力
print("材料:")
for i in range(0,len(ingredient_names)):

    # リンク付きの材料名は、改行が入ってるので、リプレイス。
    print(ingredient_names[i].text.replace("\n",""),ingredient_amounts[i].text)

# 手順を取得
steps = soup.find("div", attrs={"id": "steps"}).findAll("p", attrs={"class": "step_text"})

# 手順を出力
i = 1
print("\n手順:")
for step in steps:
    print(i, step.text)
    i += 1

