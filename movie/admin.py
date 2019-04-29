
from django.contrib import admin
from movie.models import MovieDetall, MovieKind
# Register your models here.


class MovieDetailAdmin(admin.ModelAdmin):
    pass


class MovieKindAdmin(admin.ModelAdmin):
    pass


admin.site.register(MovieDetall, MovieDetailAdmin)
admin.site.register(MovieKind, MovieDetailAdmin)

