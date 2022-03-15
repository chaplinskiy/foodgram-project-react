from django.contrib import admin

from .models import Subscription, User


class FollowingInLine(admin.TabularInline):
    model = Subscription
    fk_name = 'following'
    extra = 0


class FollowerInLine(admin.TabularInline):
    model = Subscription
    fk_name = 'follower'
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
    empty_value_display = '-пусто-'
    inlines = [FollowerInLine, FollowingInLine]


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'following', 'follower')
    search_fields = ('following',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
