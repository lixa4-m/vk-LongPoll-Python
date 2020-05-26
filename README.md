# LongPool of VK
## Install 

- Install package 'vk':
	- `pip3 install vk`
	or
	- `python3.x -m pip install vk`

- Insert GROUP TOKEN into **./configs/token.json**
- Insert LongPool version into **./longpool/config.py**
- Run:
	- `python3.x Main.py`
	
*x - your version of python3*
## Settings

- In `Main.py`:
	- `longpool.listen(True)` - all LongPool events
	- `longpool.listen()` - only messages
