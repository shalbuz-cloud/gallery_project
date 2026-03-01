from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer

from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    """
    Админ-интерфейс для модели SliderImage с сортировкой методом перетаскивания.
    """

    list_display = ("order", "image_preview", "title", "is_active", "created_at")
    list_display_links = ("title", "image_preview")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    readonly_fields = ("created_at", "updated_at", "image_preview_display")
    fieldsets = (
        (
            None,
            {
                "fields": ("title", "image", "description", "is_active"),
            },
        ),
        (
            _("Информация"),
            {
                "fields": ("image_preview_display", "created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    def image_preview_display(self, obj: SliderImage):
        """Большое превью для детальной страницы (Detail View)."""
        if obj.image:
            options = {"size": (800, 0), "upscale": False}
            try:
                thumb_url = get_thumbnailer(obj.image).get_thumbnail(options).url
                return format_html(
                    "<img src='{}' style='max-width: 100%; height: auto; "
                    "border-radius: 10px; border: 1px solid #ccc;' />",
                    thumb_url,
                )
            except Exception:
                return format_html(
                    "<a href='{}'>{}</a>", obj.image.url, _("Открыть оригинал")
                )
        return _("Нет изображения")

    image_preview_display.short_description = _("Предпросмотр изображения")

    class Media:
        css = {"all": ("css/admin.css",)}
