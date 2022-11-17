from django.db import models


# class CustomDateTimeField(models.DateTimeField):
#     def value_to_string(self, obj):
#         val = self.value_from_object(obj)
#         if val:
#             val.replace(microsecond=0)
#             return val.isoformat()
#         return ''


class DataTable(models.Model):

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class  Meta:
        ordering = ['id']
