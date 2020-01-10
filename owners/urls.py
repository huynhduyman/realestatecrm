from django.urls import path
from owners.views import (
    OwnersListView, CreateOwnerView, OwnerDetailView, OwnerUpdateView,
    OwnerDeleteView, AddCommentView, UpdateCommentView, DeleteCommentView,
    AddAttachmentView, DeleteAttachmentsView, create_mail,  # get_owner_details,
    get_contacts_for_owner, get_email_data_for_owner
)

app_name = 'owners'

urlpatterns = [
    path('', OwnersListView.as_view(), name='list'),
    path('create/', CreateOwnerView.as_view(), name='new_owner'),
    path('<int:pk>/view/', OwnerDetailView.as_view(), name="view_owner"),
    path('<int:pk>/edit/', OwnerUpdateView.as_view(), name="edit_owner"),
    path('<int:pk>/delete/', OwnerDeleteView.as_view(),
         name="remove_owner"),
    path('comment/add/', AddCommentView.as_view(), name="add_comment"),
    path('comment/edit/', UpdateCommentView.as_view(), name="edit_comment"),
    path('comment/remove/', DeleteCommentView.as_view(),
         name="remove_comment"),

    path('attachment/add/', AddAttachmentView.as_view(),
         name="add_attachment"),
    path('attachment/remove/', DeleteAttachmentsView.as_view(),
         name="remove_attachment"),
    path('create-mail', create_mail, name="create_mail"),
    path('get_contacts_for_owner/', get_contacts_for_owner,
         name="get_contacts_for_owner"),
    path('get_email_data_for_owner/', get_email_data_for_owner,
         name="get_email_data_for_owner"),
    #     path('get-owner-details/<int:owner_id>/', get_owner_details, name="get_owner_details"),

]
