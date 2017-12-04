from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import *

class Daily_Specials_Plugin(CMSPluginBase):
    model = Daily_Specials
    name = "Daily Specials"
    render_template = "daily_special.html"

    def render(self, context, instance, placeholder):
        context.update({
            'name': instance.name,
            'image': instance.image,
            'description': instance.description,
            'url': instance.url
        })

        return context

plugin_pool.register_plugin(Daily_Specials_Plugin)

