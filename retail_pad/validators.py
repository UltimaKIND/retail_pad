from rest_framework.serializers import ValidationError


class NodeValidator:
    """
    валидатор узла сети
    """

    def __call__(self, data):
        self.validate_duty_supp(data)

    def validate_duty_supp(self, data):
        """
        не может быть задолженности без указания поставщика
        """
        if not data.get("supplier") and data.get("duty_supp"):
            raise ValidationError("задолженность без поставщика?")
