ChatGPT4 | Midjourney, [10/9/2024 3:30 AM]
from typing import List, Dict, Optional

def filter_by_state(data: List[Dict], state: Optional[str] = 'EXECUTED') -> List[Dict]:
 """
 Фильтрация списка словарей по ключу "state".

 Args:
  data: Список словарей.
  state: Значение ключа "state" для фильтрации. По умолчанию 'EXECUTED'.

 Returns:
  Новый список словарей, содержащий только словари, у которых ключ "state" 
  соответствует указанному значению.
 """

 filtered_data = []
 for item in data:
  if item.get("state") == state:
   filtered_data.append(item)
 return filtered_data


Объяснение:

• from typing import List, Dict, Optional: Импортирует типы данных List, Dict и Optional для аннотации типов.
• def filter_by_state(data: List[Dict], state: Optional[str] = 'EXECUTED') -> List[Dict]:: Определяет функцию filter_by_state, которая принимает два аргумента:
  * data: List[Dict]: Список словарей, который будет отфильтрован.
  * state: Optional[str] = 'EXECUTED': Значение ключа "state" для фильтрации. По умолчанию 'EXECUTED'. Типизирован как Optional[str], поскольку может быть None.
  * -> List[Dict]: Возвращаемое значение - новый список словарей.
• """ ... """: Многострочная строка документации, описывающая функцию.
• filtered_data = []: Создает пустой список для хранения отфильтрованных словарей.
• for item in data:: Перебирает каждый словарь в data.
• if item.get("state") == state:: Проверяет, соответствует ли значение ключа "state" в текущем словаре указанному значению state.
• filtered_data.append(item): Добавляет текущий словарь в filtered_data, если его значение "state" соответствует.
• return filtered_data: Возвращает отфильтрованный список словарей.

Пример использования:

data = [
  {'id': 1, 'state': 'EXECUTED'},
  {'id': 2, 'state': 'PENDING'},
  {'id': 3, 'state': 'EXECUTED'},
  {'id': 4, 'state': 'CANCELED'},
]

filtered_data = filter_by_state(data, 'EXECUTED')

print(filtered_data)


Результат:

[{'id': 1, 'state': 'EXECUTED'}, {'id': 3, 'state': 'EXECUTED'}]

Fox, [10/9/2024 3:32 AM]
напишите аннотированную функцию 
sort_by_date
, которая принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (
date
).

ChatGPT4 | Midjourney, [10/9/2024 3:32 AM]
from typing import List, Dict, Optional

def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
 """
 Сортировка списка словарей по дате (ключ "date").

 Args:
  data: Список словарей.
  reverse: Флаг, указывающий порядок сортировки. True - по убыванию (по умолчанию), False - по возрастанию.

 Returns:
  Новый список словарей, отсортированный по дате.
 """
 return sorted(data, key=lambda item: item['date'], reverse=reverse)


Объяснение:

• from typing import List, Dict, Optional: Импортирует типы данных List, Dict и Optional для аннотации типов.
• def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:: Определяет функцию sort_by_date, которая принимает два аргумента:
  * data: List[Dict]: Список словарей, который будет отсортирован.
  * reverse: bool = True: Флаг, указывающий порядок сортировки. True - по убыванию (по умолчанию), False - по возрастанию. Типизирован как bool.
  * -> List[Dict]: Возвращаемое значение - новый список словарей.
• """ ... """: Многострочная строка документации, описывающая функцию.
• return sorted(data, key=lambda item: item['date'], reverse=reverse): Возвращает новый список, отсортированный по дате с помощью функции sorted. 
  * key=lambda item: item['date']: Указывает, что сортировка должна происходить по значению ключа "date" в каждом словаре.
  * reverse=reverse: Указывает, что порядок сортировки определяется флагом reverse.

Пример использования:

data = [
  {'id': 1, 'date': '2023-03-10'},
  {'id': 2, 'date': '2023-03-05'},
  {'id': 3, 'date': '2023-03-15'},
]

sorted_data = sort_by_date(data)

print(sorted_data)


Результат:

[{'id': 3, 'date': '2023-03-15'}, {'id': 1, 'date': '2023-03-10'}, {'id': 2, 'date': '2023-03-05'}]

Сортировка по возрастанию:

sorted_data = sort_by_date(data, reverse=False)

print(sorted_data)


Результат:

[{'id': 2, 'date': '2023-03-05'}, {'id': 1, 'date': '2023-03-10'}, {'id': 3, 'date': '2023-03-15'}]

ChatGPT4 | Midjourney, [10/10/2024 12:15 PM]
ChatGPT представили новую бесплатную нейросеть, которая создает качественные презентации всего за несколько минут 😳 @prezaprobot (https://t.me/prezaprobot?start=utmSource-telegram_utmCampaign-unlim2)

Выбор количества слайдов, языка, дизайна, изображений - всё это поможет создать уникальную презентацию в формате PowerPoint

#РЕКЛАМА
-Отключается на месяц при пополнении баланса или на год по кнопке ниже.