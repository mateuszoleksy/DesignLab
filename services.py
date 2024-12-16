import asyncio
from bleak import BleakClient

print("OK")
async def main():
	address = '38:1F:8D:58:21:34'
	async with BleakClient(address) as client:
		svcs = client.services
		print("Services:")
		for service in svcs:
			print(service)

asyncio.run(main())
