from django.db import models

NULLABLE = {"null": True, "blank": True}


class Node(models.Model):
    """
    модель узла сети
    """

    name = models.CharField(max_length=100)
    network_lvl = models.PositiveSmallIntegerField(verbose_name="уровень", **NULLABLE)
    created_at = models.DateField(auto_now_add=True)
    supplier = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="поставщик", **NULLABLE
    )
    duty_supp = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="задолженность", **NULLABLE
    )

    class Meta:
        verbose_name = "Узел сети"
        verbose_name_plural = "Узлы сети"

    def __str__(self):
        return f"{self.name}"


class Contacts(models.Model):
    """
    модель контактов узла сети
    """

    node = models.OneToOneField(Node, on_delete=models.CASCADE, related_name="contacts")
    email = models.EmailField(unique=True, verbose_name="email")
    country = models.CharField(max_length=100, verbose_name="страна")
    city = models.CharField(max_length=100, verbose_name="город")
    street = models.CharField(max_length=100, verbose_name="улица")
    house = models.CharField(max_length=100, verbose_name="номер дома")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.email}, {self.country}, {self.city}, {self.street}, {self.house}"


class Product(models.Model):
    """
    модель продукта
    """

    node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100, verbose_name="название")
    model = models.CharField(max_length=100, verbose_name="модель")
    market_entry_date = models.DateField(**NULLABLE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} {self.model}"
