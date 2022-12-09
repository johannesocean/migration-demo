from pydantic import BaseModel


class AppBaseModel(BaseModel):
    """Add a get method to BaseModel."""

    def get(self, key):
        return getattr(self, key, None)
