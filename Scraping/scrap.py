import urllib.request
from bs4 import BeautifulSoup
import time
import xlsxwriter

# Creating Work book and adding Worksheets
workbook = xlsxwriter.Workbook('agent.xlsx')
worksheet = workbook.add_worksheet()

try:
    # Assigning values to main columns and row counter
    current_row = 0
    first_col = 0
    last_col = 6

    max_row = 0
    start_row = 0

    name_col = 0
    ing_col = 1
    prod_col = 2
    prep_t_col = 3
    cook_t_col = 4
    ready_t_col = 5
    nut_col = 6
    # Adjust the column width.
    worksheet.set_column('B:B', 10)
    worksheet.set_column('C:C', 15)
    class_merge_format = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'size': 16,
        'font_name': 'Source Sans Pro',
    })

    recipe_format = workbook.add_format({
        'bold': False,
        'align': 'center',
        'valign': 'vcenter',
        'size': 12,
        'font_name': 'Source Sans Pro',
        'text_wrap': True,
    })

    merge_format = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'size': 12,
        'font_name': 'Source Sans Pro',
        'text_wrap': True,
    })

    def addone():
        global current_row
        current_row += 1

    # Main Page Link
    rec = "https://www.trustedchoice.com/agent/"

    # Creating Main Page Request Object
    while 1:
        # print('11')
        try:
            page = urllib.request.urlopen(rec)
            break
        except urllib.error.URLError:
            continue
    # print('111',page)
    # Creating bs4 object for main page
    soup = BeautifulSoup(page, features="html5lib")
    print('1111',soup)
    # Getting main links from main page
    main_div = BeautifulSoup(
        str(soup.find_all('div', {"class": "col-xs-12 col-sm-3"})), features="html5lib")

    main_links = list()
    print(main_links)
    exit()
    for anc in main_div.find_all('a'):
        main_links.append(str(anc.get("href")))
    print(main_links)

    # Iterating Through Main Links
    for class_link in main_links:
        class_rec_links = list()

        # Creating class page Request Object
        while 1:
            try:
                page = urllib.request.urlopen(class_link)
                break
            except urllib.error.URLError:
                continue

        # Creating bs4 object for class page
        soup = BeautifulSoup(page, features="html5lib")

        # Getting Class Name
        class_name = BeautifulSoup(str(soup.find('span', {
                                   "class": ["title-section__text", "title"]})), features="html5lib").get_text()
        print('###' + class_name)
        worksheet.merge_range(
            current_row, first_col, current_row, last_col, class_name, class_merge_format)
        addone()
        worksheet.merge_range(current_row, first_col,
                              current_row, last_col, '', class_merge_format)
        addone()

        # Getting recipe links from main page
        main_div = BeautifulSoup(str(soup.find_all(
            'h3', {"class": ["fixed-recipe-card__h3"]})), features="html5lib")
        for anc in main_div.find_all('a'):
            class_rec_links.append(str(anc.get("href")))
        print(class_rec_links)

        # Iterating through recipe pages
        for link in class_rec_links:

            time.sleep(0.25)
            # Get Name of Recipe
            while 1:
                try:
                    while 1:
                        page = urllib.request.urlopen(link)
                        if page:
                            break
                    break
                except urllib.error.URLError:
                    continue
            print(link)

            soup = BeautifulSoup(page, features="html5lib")
            name = BeautifulSoup(str(soup.find(
                'h1', {"id": ["recipe-main-content"]})), features="html5lib").get_text()
            print(name)

            # Get Ingredients of Recipe
            ingredients = list()
            for label in soup.select('span.recipe-ingred_txt'):
                ingredients.append(label.text)
            ingredients = ingredients[:-3]
            # print(len(ingredients))

            # Adding ingredients to excel
            start_row = current_row
            for x in ingredients:
                worksheet.write(current_row, ing_col, x, recipe_format)
                addone()
            max_row = current_row

            # Get procedure of Recipe
            procedure = list()
            proc = BeautifulSoup(str(soup.find('ol', {"class": [
                                 "list-numbers", "recipe-directions__list"], "itemprop": ["recipeInstructions"]})), features="html5lib")
            for step in proc.select('span.recipe-directions__list--item'):
                procedure.append(step.text.replace('\n', '').strip())
            # print(procedure)

            # Adding procedure to excel
            current_row = start_row
            for x in procedure:
                worksheet.write(current_row, prod_col, x, recipe_format)
                addone()
            if max_row < current_row:
                max_row = current_row

            # Get Time to cook of Recipe
            times = list()
            inc = [1, 3, 5]
            count = 0
            current_row = start_row
            for timer in soup.select('li.prepTime__item span'):
                if count in inc:
                    times.append(timer.text)
                count += 1
            print(times)

            if len(times) != 0:
                # Inserting Time to Excel
                try:
                    worksheet.write(current_row, prep_t_col,
                                    times[0], recipe_format)  # Preparation Time
                    worksheet.write(current_row, cook_t_col,
                                    times[1], recipe_format)  # Cook Time
                    # Ready to cook Time
                    worksheet.write(current_row, ready_t_col,
                                    times[2], recipe_format)
                except IndexError:
                    continue

            # Get Nutrition of Recipe
            nutri = BeautifulSoup(
                str(soup.find('div', {"class": "nutrition-summary-facts"})), features="html5lib")
            nutrition = ' '.join(nutri.get_text().split()
                                 ).replace('Full nutrition', '')
            # print(nutrition)

            # Add nutrition to excel
            worksheet.write(current_row, nut_col, nutrition, recipe_format)

            # Add name to excel
            worksheet.merge_range(start_row, first_col,
                                  max_row, first_col, name, merge_format)
            current_row = max_row
            addone()

    workbook.close()
except:
    workbook.close()
