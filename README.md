BLE Blood Pressure Monitor
==========================

Overview
--------

This project is a **Bluetooth Low Energy (BLE) blood pressure monitor** reader written in Python. It connects to a BLE-enabled blood pressure monitor, retrieves measurement data, and decodes it according to the **IEEE 11073-20601**standard.

Features
--------

*   Connects to a **BLE blood pressure monitor**.
    
*   Reads **systolic, diastolic, and mean arterial pressure** values.
    
*   Retrieves **pulse rate** (if available).
    
*   Extracts **measurement timestamp** (if provided by the device).
    
*   Supports standard **GATT blood pressure service (0x1810)**.
    

Requirements
------------

*   Python 3.7+
    
*   [Bleak](https://github.com/hbldh/bleak) (Python BLE library)
    

Install dependencies:

    pip install bleak

Usage
-----

1.  Turn on your BLE-enabled blood pressure monitor.
    
2.  Find your device's MAC address using a BLE scanner (or modify the script to scan automatically).
    
3.  Run the script:
    
        python main.py
    

Example Output
--------------

    ✅ Connected to A99A7D42-8DA5-787A-B1D5-D5198E11696C
    ⏳ Waiting for blood pressure data... (Press CTRL+C to exit)
    📥 Raw Data: bytearray(b'\x1e\x83\x00=\x00`\x00\xe9\x07\x02\x02\x15\x0c\x00V\x00\x01\x04\x00')
    📊 Blood Pressure: 131/61 (96 mmHg)
    📆 Measurement Time: 2024-02-02 12:00:00
    💓 Pulse: 86 bpm

Supported Devices
-----------------

This script should work with **any BLE blood pressure monitor** that follows the standard **Blood Pressure Service (0x1810)**. It has been tested with:

*   **Medisana BU 570**
    

License
-------

This project is licensed under the **MIT License**. Feel free to use and modify it!

Disclaimer
----------

This script is intended for **educational and development purposes only**. It is not a certified medical application and should not be used for diagnosis or treatment.


Author
----------

Martin Hocquel-Hans
