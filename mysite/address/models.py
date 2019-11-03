from django.db import models

class Address(models.Model):
    postal_code = models.CharField(
        verbose_name = "郵便番号",
        max_length = 7,
    )
    region = models.CharField(
        verbose_name = "都道府県",
        max_length = 4,
    )
    locality = models.CharField(
        verbose_name = "市町村",
        max_length = 10,
    )
    street = models.CharField(
        verbose_name = "番地",
        max_length = 40,
    )
    extended = models.CharField(
        verbose_name = "建物",
        max_length = 40,
    )