from django.urls import include, path
from  .views import AttendeesBook, AttendeesList, AttendeesDelete

urlpatterns = [
    path('bookTicket/', AttendeesBook.as_view(), name="book-ticket"),
    path('', AttendeesList.as_view()),
    path('delete/<int:pk>/', AttendeesDelete.as_view())
]
