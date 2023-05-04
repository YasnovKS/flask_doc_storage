from .models import Document


def data_is_valid(data: dict, obj: Document) -> bool:
    versions = obj.versions
    last_version = versions[0].to_dict()
    return any(
        [
            value != last_version.get(key)
            for key, value in data.items()
        ]
    )
