from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()

# Call the reload method to ensure objects are loaded from the JSON file
storage.reload()
