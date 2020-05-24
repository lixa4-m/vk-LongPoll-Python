#!/bin/python3
import traceback
import configs
import longpool

print('Token:', configs.tokens())

for message in longpool.listen():
	print()
	print(message)
	print(f"\npeer_id: {message['peer_id']}\nText: {message['text']}")

# or

for updates in longpool.listen():
	print()
	print(updates)
