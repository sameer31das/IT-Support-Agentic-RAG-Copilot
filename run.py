from app.core.config import get_settings

settings = get_settings()

print("Settings loaded:")
print(f"App Name: {settings.app_name}")
