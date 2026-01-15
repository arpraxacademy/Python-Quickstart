"""
Project 5: Smart Home System
Part of the 'Python Fast Track' Bootcamp by Arprax Academy.

📺 Watch the Tutorial for this Script: https://youtu.be/YMNSBsjbO4E
▶️ Full Course Playlist: https://youtube.com/playlist?list=PL7kitcmP3RiO724GV3Fmb1MHEp0g9RYnJ&si=ozyOr1brpt0lUbEH

Description:
A complete OOP example demonstrating the 4 Pillars (A.P.I.E.):
- Abstraction (Blueprints)
- Polymorphism (Common Interface)
- Inheritance (Shared Code)
- Encapsulation (Private Variables)
"""

from abc import ABC, abstractmethod


# -------------------------------
# A: Abstraction (The Blueprint)
# -------------------------------
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
        self.is_on = False  # Shared Attribute
        self.wifi_connected = False  # Shared Attribute

    # Inheritance: All children get this method for free
    def connect_to_wifi(self, network_name):
        self.wifi_connected = True
        print(f"📡 {self.name} connected to wifi network {network_name}")

    # Abstract Method: Enforces that children MUST create this function
    @abstractmethod
    def turn_on(self):
        pass

    def turn_off(self):
        self.is_on = False
        print(f"🔴 {self.name} turned off")


# -------------------------------
# I: Inheritance (Shared Features)
# -------------------------------
class SmartLight(SmartDevice):
    def turn_on(self):
        print(f"💡 {self.name} is glowing warm white")


class SmartSpeaker(SmartDevice):
    def turn_on(self):
        # Polymorphism: Same method name, different behavior
        print(f"🎵 {self.name} is playing your favorite playlist.")


# -------------------------------
# E: Encapsulation (Data Protection)
# -------------------------------
class SmartThermostat(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        # Double underscore makes this variable PRIVATE.
        # It cannot be changed directly from outside.
        self.__temperature = 72

    def turn_on(self):
        self.is_on = True
        print(f"🌡️ {self.name} is running. Target Temp: {self.__temperature}F")

    # Setter: Protects the data with validation logic
    def set_temperature(self, new_temperature):
        if 60 <= new_temperature <= 80:
            self.__temperature = new_temperature
            print(f"✅ Temperature set to {self.__temperature}F")
        else:
            print(f"❌ Denied: {new_temperature}F is not a safe temperature.")

    # Getter: Allows read-only access to private data
    def get_temperature(self):
        return self.__temperature


if __name__ == "__main__":
    # Creating Objects
    light = SmartLight("Living Room Light")
    speaker = SmartSpeaker("Kitchen Alexa")
    thermostat = SmartThermostat("Hallway Nest")

    # Demo: Inheritance
    print("\n[Inheritance] Connecting devices to WiFi...")
    light.connect_to_wifi("MyHome_5G")
    speaker.connect_to_wifi("MyHome_5G")
    thermostat.connect_to_wifi("MyHome_5G")

    # -------------------------------
    # P: Polymorphism
    # -------------------------------
    print("\n[Polymorphism] Turning everything on...")
    # Treat different devices as the same type
    devices = [light, speaker, thermostat]
    for device in devices:
        device.turn_on()

    # Demo: Encapsulation
    print("\n[Encapsulation] Adjusting Thermostat...")

    # 1. Safe change
    thermostat.set_temperature(75)

    # 2. Unsafe change (The Setter logic rejects this)
    thermostat.set_temperature(500)

    # 3. Direct access attempt (Simulating a hack)
    try:
        print(thermostat.__temperature)
    except AttributeError:
        print("🔒 Error: Cannot access private variable '__temperature' directly.")