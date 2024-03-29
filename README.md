# i3wm-configs
my configs for the i3 window manager

**instructions (currently running on ubuntu 20.04):**

The following applications are used in addition to i3:
  
  * *i3blocks* (`sudo apt install i3blocks`)
  * *conky* (`sudo apt install conky`) for the i3bar-stuff (not needed if you use i3blocks)
  * *udiskie* (`sudo apt install udiskie`) for USB-mounts
  * *redshift* (`sudo apt install redshift`) for color adjustments.
  * *i3lock* (`sudo apt install i3lock`) for lock screen

**installation:**

  * copy *config* into ~/.config/i3/
  * copy *conkyrc* into ~/.config/conky/
  * copy *cpuinfo.sh*, *cputemp.py*, *lock_screen*, *conky-i3bar*, *get_volume.sh*, *volume_bar.py*, *update-check*, *start_i3blocks.sh*, *mpdinfo.sh*, *i3blocks_jack.sh* and *i3blocks_connections.sh* in a directory that's included in $PATH (I use ~/bin/) and make them executable (cpuinfo, cputemp, conky-i3bar are not needed when using i3blocks, start_i3blocks.sh, i3blocks_jack.sh and i3blocks_connections.sh when using conky)
  * copy *lock_circle.png* into ~/.config/i3/
  * copy i3blocksconfig into ~/.config/i3blocks/config

