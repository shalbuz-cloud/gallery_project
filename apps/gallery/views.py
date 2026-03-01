from django.views.generic import TemplateView

from .models import SliderImage


class GalleryView(TemplateView):
    """
    Представление для отображения страницы галереи со слайдером.
    """

    template_name = "gallery/index.html"

    def get_context_data(self, **kwargs):
        """Добавляет изображения слайдера в контекст."""
        context = super().get_context_data(**kwargs)
        context["slider_images"] = SliderImage.objects.filter(
            is_active=True
        ).select_related("image")
        return context
