from users.models import User
from django.core.management import BaseCommand
from typing import Any, Optional


class Command(BaseCommand):
    help = "Creates a defauld admin user"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write(self.style.WARNING("Criando usuário administrador..."))

        admin_data = {
            "username": "admin",
            "email": "admin@mail.com",
            "password": "admin1234",
            "first_name": "Administrador",
        }

        find_adm = User.objects.filter(is_superuser=True)
        if not find_adm:
            User.objects.create_superuser(**admin_data)
            self.stdout.write(self.style.SUCCESS("Administrador criado com sucesso!"))
        else:
            self.stdout.write(self.style.WARNING("Usuário administrador já existe!"))
