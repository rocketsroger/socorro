from django.conf.urls import url

from . import views


app_name = 'manage'
urlpatterns = [
    url('^$',
        views.home,
        name='home'),
    url('^users/$',
        views.users,
        name='users'),
    url('^users/data/$',
        views.users_data,
        name='users_data'),
    url('^users/(?P<id>\d+)/$',
        views.user,
        name='user'),
    url('^groups/$',
        views.groups,
        name='groups'),
    url('^groups/(?P<id>\d+)/$',
        views.group,
        name='group'),
    url('^analyze-model-fetches/$',
        views.analyze_model_fetches,
        name='analyze_model_fetches'),
    url('^graphics-devices/$',
        views.graphics_devices,
        name='graphics_devices'),
    url('^graphics-devices/lookup/$',
        views.graphics_devices_lookup,
        name='graphics_devices_lookup'),
    url('^supersearch-fields/missing/$',
        views.supersearch_fields_missing,
        name='supersearch_fields_missing'),
    url('^products/$',
        views.products,
        name='products'),
    url('^releases/$',
        views.releases,
        name='releases'),
    url('^events/$',
        views.events,
        name='events'),
    url('^events/data/$',
        views.events_data,
        name='events_data'),
    url('^api-tokens/$',
        views.api_tokens,
        name='api_tokens'),
    url('^api-tokens/delete/$',
        views.api_tokens_delete,
        name='api_tokens_delete'),
    url('^api-tokens/data/$',
        views.api_tokens_data,
        name='api_tokens_data'),
    url('^status/$',
        views.status_message,
        name='status_message'),
    url('^status/disable/(?P<id>\d+)/$',
        views.status_message_disable,
        name='status_message_disable'),
    url('^crash-me-now/$',
        views.crash_me_now,
        name='crash_me_now'),
    url('^reprocessing/$',
        views.reprocessing,
        name='reprocessing'),

]
