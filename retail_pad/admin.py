from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from retail_pad.models import Node, Product


@admin.register(Node)
class Node(admin.ModelAdmin):
    """
    регистрация модели Node в админке
    """

    list_display = ("name", "supplier_link", "duty_supp", "contacts__city")
    search_fields = ("contacts__city",)
    actions = ["clear_duty"]

    def clear_duty(self, request, queryset):
        """
        очищает задолженность
        """
        queryset.update(duty_supp=0)

    clear_duty.short_description = "очистить задолженность перед поставщиком"

    def supplier_link(self, obj):
        """
        ссылка на поставщика
        """
        from django.utils.html import format_html

        url = reverse("admin:retail_pad_node_changelist") + f"{obj.id}"
        if obj.supplier:
            return format_html('<a href="{}">{} </a>', url, obj.supplier)
        else:
            return None

        supplier_link.short_description = "Ссылка на поставщика"


@admin.register(Product)
class Product(admin.ModelAdmin):
    """
    регистрация модели Product в админке
    """

    list_display = ("name", "model", "node", "market_entry_date")