from typing import Dict, List, Optional


def filter_by_state(data: List[Dict], state: Optional[str] = "EXECUTED") -> List[Dict]:
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


data = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "PENDING"},
    {"id": 3, "state": "EXECUTED"},
    {"id": 4, "state": "CANCELED"},
]

filtered_data = filter_by_state(data, "EXECUTED")

print(filtered_data)


from typing import Dict, List, Optional


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортировка списка словарей по дате (ключ "date").

    Args:
     data: Список словарей.
     reverse: Флаг, указывающий порядок сортировки. True - по убыванию (по умолчанию), False - по возрастанию.

    Returns:
     Новый список словарей, отсортированный по дате.
    """
    return sorted(data, key=lambda item: item["date"], reverse=reverse)


data = [
    {"id": 1, "date": "2023-03-10"},
    {"id": 2, "date": "2023-03-05"},
    {"id": 3, "date": "2023-03-15"},
]

sorted_data = sort_by_date(data)

print(sorted_data)


sorted_data = sort_by_date(data, reverse=False)

print(sorted_data)
