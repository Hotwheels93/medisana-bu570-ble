# Author: Martin Hocquel-Hans
# Date: 2025-02-02
# Description: This script connects to Medisana BU 570 blood pressure monitor and reads blood pressure data and pulse rate as well as the timestamp of the measurement.
# License: MIT


import asyncio
import struct
from bleak import BleakClient
from datetime import datetime

DEVICE_ADDRESS = "A99A7D42-8DA5-787A-B1D5-D5198E11696C"
BLOOD_PRESSURE_MEASUREMENT_UUID = "00002A35-0000-1000-8000-00805F9B34FB"  # 0x2A35

def parse_blood_pressure(data):
    """ Decode measurement (IEEE 11073-20601) """
    flags = data[0]  # First byte is the flags field
    unit = "mmHg" if (flags & 0x01) == 0 else "kPa"

    # Basic measurement values (systolic, diastolic, mean arterial pressure)
    systolic, diastolic, mean_arterial = struct.unpack_from("<HHH", data, 1)

    index = 7  # Start index after basic measurement values

    # Timestamp available?
    if flags & 0x02:
        year, month, day, hour, minute, second = struct.unpack_from("<HBBBBB", data, index)
        timestamp = datetime(year, month, day, hour, minute, second)
        index += 7
    else:
        timestamp = None

    # Pulse rate available?
    if flags & 0x04:
        pulse, = struct.unpack_from("<H", data, index)
        index += 2
    else:
        pulse = None

    # User ID available? (Optional, usually not used)
    if flags & 0x08:
        user_id = data[index]
        index += 1
    else:
        user_id = None

    # Status available? (Optional, usually not used)
    if flags & 0x10:
        status, = struct.unpack_from("<H", data, index)
    else:
        status = None

    return systolic, diastolic, mean_arterial, pulse, timestamp, unit

async def notification_handler(sender, data):
    """ Callback for blood pressure measurement notifications """
    print(f"📥 Raw data: {data}")

    systolic, diastolic, mean_arterial, pulse, timestamp, unit = parse_blood_pressure(data)

    print(f"📊 Bloodpressure: {systolic}/{diastolic} ({mean_arterial} {unit})")
    if pulse:
        print(f"💓 Pulse: {pulse} bpm")
    if timestamp:
        print(f"📅 Datetime: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

async def main():
    async with BleakClient(DEVICE_ADDRESS) as client:
        print(f"✅ Connected with {DEVICE_ADDRESS}")

        # Activate notifications for blood pressure measurements 0x2A35 (Blood Pressure Measurement)
        await client.start_notify(BLOOD_PRESSURE_MEASUREMENT_UUID, notification_handler)

        print("⏳ Waiting for notifications... (Press Ctrl+C to stop)")
        await asyncio.sleep(60)  # Listen for 60 seconds

asyncio.run(main())

