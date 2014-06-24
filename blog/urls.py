from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^new_post/$', views.CreatePost.as_view(), name="new_post"),
    url(r'^new_tag/$', views.CreateTag.as_view(), name="new_tag"),
    url(r'^taglist/$', views.TagList.as_view(), name="taglist"),
    url(r'^posts/$', views.PostList.as_view(), name="postlist"),
    #url(r'^(?P<pk>)/$', views.PostView.as_view(), name="postview"),
    url(r'^edit/(?P<pk>\d+)/$', views.PostEdit.as_view(), name="postedit"),
 	url(r'^delete/(?P<pk>\d+)/$', views.PostDelete.as_view(), name="postdelete"),
 	url(r'^contact/$', views.ContactView.as_view(), name="contact"),
)
