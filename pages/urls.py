from django.urls import path

from . import views

pages_patterns = ([
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('create/', views.CreatePageView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdatePageView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeletePageView.as_view(), name='delete'),
], 'pages')
