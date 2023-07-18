import os
import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


def to_slug(name: str) -> str:
    return name.lower().strip().replace(' ', '-')


class Command(BaseCommand):
    def add_arguments(self, parser):
        """Получает имя csv-файла с данными для загрузки.
           По умолчанию - 'phones.csv'."""
        parser.add_argument(
            'file_name',
            action='store',
            nargs='?',
            default='phones.csv',
            help='Название файла для считывания данных'
        )

    def handle(self, *args, **options):
        """Переносит данные из csv-файла в модель (таблицу БД) Phone."""
        input_file = options['file_name']
        if not os.path.exists(input_file):
            self.stdout.write(f"Файл не найден\n{input_file}")
            return
        with open(input_file, 'r', encoding="utf-8") as phones_file:
            phones = list(csv.DictReader(phones_file, delimiter=';'))
        for phone in phones:
            Phone.objects.create(name=phone['name'],
                                 image=phone['image'],
                                 price=phone['price'],
                                 release_date=phone['release_date'],
                                 lte_exists=phone['lte_exists'],
                                 # TODO: Добавить создание поля Slug. ... Сделал 18.07.23
                                 # Не дошёл до 'Преобразователя путей по умолчанию'. Сделал "в лоб", написал своё.
                                 # slug=to_slug(phone['name'])    # Переопределил метод save(). 18.07.23
            )
            # Считывание и обновление отдельного параметра.
            # Phone.objects.filter(id=phone['id']).update(slug=to_slug(phone['name']))
        self.stdout.write("Данные перенесены.")    # Для теста.
        return
