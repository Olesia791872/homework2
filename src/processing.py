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




Пример использования:

data = [
  {'id': 1, 'state': 'EXECUTED'},
  {'id': 2, 'state': 'PENDING'},
  {'id': 3, 'state': 'EXECUTED'},
  {'id': 4, 'state': 'CANCELED'},
]

filtered_data = filter_by_state(data, 'EXECUTED')

print(filtered_data)


