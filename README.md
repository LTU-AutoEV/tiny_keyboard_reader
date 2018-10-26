# `tiny_keyboard_reader`

*A tiny no-dependency package for publishing keyboard input*

The package uses the `curses` library provided in Python 2 to read the keyboard. The launch file automatically launches the node in a separate xterm window. This window must be active to read and publish data.

To launch:

```
roslaunch tiny_keyboard_reader keyboard_reader.launch
```
