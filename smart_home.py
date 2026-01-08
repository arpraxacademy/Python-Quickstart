from abc import ABC, abstractmethod
# -------------------------------
# A: Abstraction
# -------------------------------
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
        self.is_on = False # Shared Attribute
        self.wifi_connected = False # Shared Attribute
    # Inheritance
    def connect_to_wifi(self, network_name):
        self.wifi_connected = True
        print(f"📡 {self.name} connected to wifi network {network_name}")

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
        # Implementation specific to a Speaker
        print(f"🎵 {self.name} is playing your favorite playlist.")
# -------------------------------
# E: Encapsulation (Data Protection)
# -------------------------------
class SmartThermostat(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__temperature = 72 # __Variable is PRIVATE
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
    light = SmartLight("light")
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
    devices = [light, speaker, thermostat]
    for device in devices:
        device.turn_on()

    # Demo: Encapsulation
    # Trying to hack the thermostat
    print("\n[Encapsulation] Adjusting Thermostat...")

    # 1. Safe change
    thermostat.set_temperature(75)
    # 2. Unsafe change (Logic protects the variable)
    thermostat.set_temperature(500)
    # 3. Direct access attempt (Simulating a hack)
    try:
        print(thermostat.__temperature)
    except AttributeError:
        print("🔒 Error: Cannot access private variable '__temperature' directly.")