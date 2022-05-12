# coding=utf-8
from django.contrib import admin
from django.db.models import QuerySet

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    '''Для настройки админской панели!'''

    # list_display -> Отображение на панеле
    list_display = ('author', 'category')

    # list_display_links -> Переобразовать в ссылку
    list_display_links = ['author', 'category']

    # search_fields -> Поиск болгондо кайсылардан издеш керек!
    search_fields = ('author', 'description', 'author_text',)

    # list_filter -> Фильтр для отображения
    list_filter = ('category',)

    # list_per_page -> Бир страницада канча запись болуш керек
    list_per_page = 10

    # actions -> Кайсы дествиялар болуш керек
    actions = ['set_category_LifeStyle',
               'set_category_Food',
               'set_category_Healthy',
               'set_category_sport',
               'set_category_Entertaiment',
               'set_clone_model',
               ]

    # Добавление дествии

    @admin.action(description='Установить категорию LifeStyle')
    def set_category_LifeStyle(self, request, qs: QuerySet):
        qs.update(category=1)

    @admin.action(description='Установить категорию Food')
    def set_category_Food(self, request, qs: QuerySet):
        qs.update(category=2)

    @admin.action(description='Установить категорию Healthy')
    def set_category_Healthy(self, request, qs: QuerySet):
        qs.update(category=3)

    @admin.action(description='Установить категорию Entertaiment')
    def set_category_Entertaiment(self, request, qs: QuerySet):
        qs.update(category=5)

    @admin.action(description='Установить категорию Sport')
    def set_category_sport(self, request, qs: QuerySet):
        count_updates = qs.update(category=4)
        # self.message_user -> Функция болгондо кандай сообщение чыгарына жооп берет.
        self.message_user(request,
                          f'Было обновлено {count_updates} записей',

                          )

    @admin.action(description='Копировать как новый модель')
    def set_clone_model(self, request, qs: QuerySet):
        for object in qs:
            object.id = None
            object.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
