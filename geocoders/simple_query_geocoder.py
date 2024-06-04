from geocoders.geocoder import Geocoder
from api import API

# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        try:
            node = API.get_area(area_id)
        except Exception as e:
            # Обработка ошибки при получении данных из API
            print(f"Error getting area data: {e}")
            return ""

        address_parts = [node.name]

        while node.parent_id is not None:
            try:
                node = API.get_area(node.parent_id)
                address_parts.append(node.name)
            except Exception as e:
                # Обработка ошибки при получении данных из API
                print(f"Error getting parent area data: {e}")
                break

        address = ", ".join(reversed(address_parts))
        return address