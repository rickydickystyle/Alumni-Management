from rest_framework.pagination import PageNumberPagination


class AlumniPaginator(PageNumberPagination):
    page_size = 3