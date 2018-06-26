from import_export import resources
from .models import Salary


class SalaryResource(resources.ModelResource):
    class Meta:
        model = Salary
