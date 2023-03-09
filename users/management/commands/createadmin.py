from users.models import User
from django.core.management import BaseCommand
from typing import Any, Optional
import os


class Command(BaseCommand):
    help = "Creates a defauld admin user"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write(self.style.WARNING("Criando usuário administrador..."))

        admin_data = {
            "username": os.getenv("ADMIN_USERNAME"),
            "email": os.getenv("ADMIN_EMAIL"),
            "password": os.getenv("ADMIN_PASSWORD"),
            "first_name": os.getenv("ADMIN_FIRST_NAME"),
            "image": os.getenv("ADMIN_IMAGE"),
        }

        find_adm = User.objects.filter(is_superuser=True)
        if not find_adm:
            User.objects.create_superuser(**admin_data)
            self.stdout.write(self.style.SUCCESS("Administrador criado com sucesso!"))
        else:
            self.stdout.write(self.style.WARNING("Usuário administrador já existe!"))
