# LongPool of VK
## Install 
Install package 'vk':
..`pip install vk`
Insert GROUP TOKEN into **./configs/token.json**
Insert LongPool version into **./longpool/config.py**
Run.
`python3 Main.py`

## Settings

- In `Main.py`:
	- `longpool.listen(True)` - all LongPool events
	- `longpool.listen()` - only messages