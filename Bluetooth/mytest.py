import asyncio
from bleak import BleakScanner

# 用于存储已经扫描到的设备地址
scanned_devices = set()

async def scan_forever():
    while True:
        devices = await BleakScanner.discover()
        for device in devices:
            if device.address not in scanned_devices:
                print(f"设备名称: {device.name}, MAC 地址: {device.address}")
                scanned_devices.add(device.address)

asyncio.run(scan_forever())
