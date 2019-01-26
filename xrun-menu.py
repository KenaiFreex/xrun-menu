#!/usr/bin/python

# Import the necessary packages
from cursesmenu import *
from cursesmenu.items import *

# Create the menu
menu = CursesMenu("GPU SELECTOR", "Select your gpu to start X session")

# You can add a custom item according to your needs
#custom_command_item = CommandItem("Message",  "command")

# For example, adding a XFCE otion to run with Nvidia GPU
#xfce_item = CommandItem("Nvidia XFCE (nvidia-xrun)",  "nvidia-xrun startxfce4")

#My entries

intel_item = CommandItem("Intel (SDDM)",  "startx")
nvidia_kde_item = CommandItem("Nvidia KDE (nvidia-xrun)",  "nvidia-xrun startkde")
nvidia_i3_item = CommandItem("Nvidia i3WM (nvidia-xrun)",  "nvidia-xrun startkde")


#After create yout entries, you need to append it to the menu

menu.append_item(intel_item)
menu.append_item(nvidia_kde_item)
menu.append_item(nvidia_i3_item)

#For example, append the custom item for xfce created above.
#menu.append_item(xfce_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()

