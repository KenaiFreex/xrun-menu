# xrun-menu
Tool based on python-menu to select with which GPU to initiate an X session to boot the system in manjaro using xrun

# this tool has only been tested on manjaro with "mhwd -a pci nonfree 0300"


First we have to make sure that we have installed the non-free manjaro drivers by executing the following command

```bash
sudo mhwd -a pci nonfree 0300
```
# Install dependencies:
you can change trizen by any AUR manager

```bash
sudo pacman -S trizen git python python-pip
```
Then
```bash
trizen -S nvidia-xrun-pm
sudo pip install curses-menu

```
# Install menu

```bash
git clone https://github.com/KenaiFreex/xrun-menu.git
cd xrun-menu
sudo cp xrun-menu /usr/bin/xrun-menu
sudo chmod +x /usr/bin/xrun-menu

```
After installing xrun-menu to /usr/bin/xrun-menu

We need to configure the system to start in console mode by executing the following commands
```
systemctl set-default multi-user.target
```
```bash
systemctl edit getty@tty1

```
and fill it with following lines, don't forget to change "you-username" with your actual username
```
[Service]
ExecStart=
ExecStart=-/usr/bin/agetty --autologin you-username --noclear %I $TERM
```
This will cause your system to start in console mode, so we need to make xrun-menu start at the same time as your user session,for this you will have to modify your bash profile That is in the following path.
```
nano ~/.bash_profile
```
and you will have to add "xrun-menu" to the end of the file:

```
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

xrun-menu
```
And you're finished. Restart and enjoy your personalized menu


# Custom Menu Entries

You can modify the menu entries at any time by modifying the binary in "/usr/bin/ xrun-menu" 
```
sudo nano /usr/bin/xrun
```

Which contains the following content

```python
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

```

