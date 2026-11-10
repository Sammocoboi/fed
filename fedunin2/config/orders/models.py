from django.db import models
import uuid 

class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    product = models.CharField(max_length=50)

    status=models.CharField(max_length=50,default="queued",choices=[
                                        ("queue","в очереди"),
                                        ("process","в обработке"),
                                        ("done","готов"),
                                        ("publish_error","ошибка публикации")])

    create-at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} = {self.status}"