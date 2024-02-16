#!/usr/bin/env python3

import os

# Specify the path to your virtual environment
# venv_path = "path/to/your/env"
venv_path = '/home/adminuser/Developements/Nuxt3'


print('venv_ path ',  venv_path)


# Check if the virtual environment exists
if os.path.isdir(venv_path):
    # Activate the virtual environment
    activate_script = os.path.join(venv_path, "bin", "activate")
    activate_cmd = f"source {activate_script}"

    # Execute the activation command
    os.system(activate_cmd)
    print("Virtual environment activated!")
else:
    print(f"Error: Virtual environment not found at {venv_path}")


# if __name__ == "__main__":
#     pass


#!/usr/bin/env python3

# import os

# class VirtualEnvironmentActivator:
#     def __init__(self, venv_path):
#         self.venv_path = venv_path

#     def activate_virtual_environment(self):
#         # Check if the virtual environment exists
#         if os.path.isdir(self.venv_path):
#             # Activate the virtual environment
#             activate_script = os.path.join(self.venv_path, "bin", "activate")
#             activate_cmd = f"source {activate_script}"

#             # Execute the activation command
#             os.system(activate_cmd)
#             print("Virtual environment activated!")
#         else:
#             print(f"Error: Virtual environment not found at {self.venv_path}")

# def main():
#     # Specify the path to your virtual environment
#     venv_path = "path/to/your/env"

#     # Create an instance of VirtualEnvironmentActivator
#     activator = VirtualEnvironmentActivator(venv_path)

#     # Activate the virtual environment
#     activator.activate_virtual_environment()

# if __name__ == "__main__":
#     main()
