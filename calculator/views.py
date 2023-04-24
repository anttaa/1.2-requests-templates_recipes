from django.shortcuts import render
from django.urls import reverse

DATA = {
    "omlet": {
        "яйца, шт": 2,
        "молоко, л": 0.1,
        "соль, ч.л.": 0.5,
    },
    "pasta": {
        "макароны, г": 0.3,
        "сыр, г": 0.05,
    },
    "buter": {
        "хлеб, ломтик": 1,
        "колбаса, ломтик": 1,
        "сыр, ломтик": 1,
        "помидор, ломтик": 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    template_name = "home.html"
    pages = []
    for item in DATA:
        pages.append(item)
    context = {"pages": pages}
    return render(request, template_name, context)


def receipt_view(request, name):
    servings = int(request.GET.get("servings", 1))

    context = {"recipe": "", "pages": {"Главная страница": reverse("home")}}

    if name in DATA:
        context["recipe"] = DATA[name]
        for item in context["recipe"]:
            context["recipe"][item] *= servings

    return render(request, "calculator/index.html", context)
