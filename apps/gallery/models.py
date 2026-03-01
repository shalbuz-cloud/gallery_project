from easy_thumbnails.files import get_thumbnailer
from filer.fields.image import FilerImageField

from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class SliderImage(models.Model):
    """
    Модель для слайдера изображений с возможностью сортировки.
    """

    title = models.CharField(
        max_length=255,
        verbose_name=_("Название"),
        help_text=_("Введите название изображения"),
    )
    image = FilerImageField(
        on_delete=models.CASCADE,
        related_name="slider_images",
        verbose_name=_("Изображения"),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Описание"),
        help_text=_("Введите описание изображения (необязательно)"),
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Порядок сортировки"),
        db_index=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Активно"),
        help_text=_("Отображать ли изображение в слайдере"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата создания"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Дата обновления"),
    )

    def image_preview(self):
        """Возвращает HTML-код для предварительного просмотра изображения в админке."""
        if self.image:
            try:
                # Генерируем маленькое превью 100x100 (умная обрезка по центру)
                options = {"size": (100, 100), "crop": True}
                thumb_url = get_thumbnailer(self.image).get_thumbnail(options).url
                return format_html(
                    "<img src='{}' width='100' height='100' "
                    "stype='object-fit: cover; border-radius: 8px;' />",
                    thumb_url,
                )
            except Exception:
                return _("Ошибка загрузки")
        return _("Нет изображения")

    image_preview.short_description = _("Превью")
    image_preview.allow_tags = True

    class Meta:
        verbose_name = _("Изображение слайдера")
        verbose_name_plural = _("Изображения для слайдера")
        ordering = ["order", "-created_at"]

    def __str__(self) -> str:
        """Строковое представление модели."""
        return self.title
