#!/usr/bin/python3
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# Create a FileStorage instance
storage = FileStorage()

# Ensure the environment is clean (Optional)
if os.path.exists(storage._FileStorage__file_path):
    os.remove(storage._FileStorage__file_path)

# Initial reload to start with a clean or known state
storage.reload()

# Create new objects
obj1 = BaseModel()
obj2 = BaseModel()

# Manually add objects to storage if necessary
storage.new(obj1)
storage.new(obj2)

# Save the current state
storage.save()

# Reload to simulate retrieving persisted objects
storage.reload()

# Verify the objects are still accessible
# This step depends on how you access objects, assuming a method like `all()` exists
all_objects = storage.all()
assert f"BaseModel.{obj1.id}" in all_objects, "obj1 is missing after first reload"
assert f"BaseModel.{obj2.id}" in all_objects, "obj2 is missing after first reload"

# Save again to test persistence
storage.save()

# Final reload to ensure persistence across multiple operations
storage.reload()

# Final verification
all_objects = storage.all()
assert f"BaseModel.{obj1.id}" in all_objects, "obj1 is missing after second reload"
assert f"BaseModel.{obj2.id}" in all_objects, "obj2 is missing after second reload"

print("Reload, save, reload sequence test passed.")