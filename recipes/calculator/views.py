from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
def recipe_view(request):
    tmp_var = request.path[1:-1]
    context = {}
    if 'servings' in request.GET:
        tmp_servings = int(request.GET['servings'])
    else:
        tmp_servings = 1
    for key in DATA.keys():
        if key == tmp_var:
            recipe = DATA[key]
            for key, value in recipe.items():
                recipe[key] = float(value) * tmp_servings
            context.update({'recipe': recipe})
    return render(request,"calculator/index.html", context)

# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def home_page_view(request):
    return render(request, 'calculator/home_page.html')