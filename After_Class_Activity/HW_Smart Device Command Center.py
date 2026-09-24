from abc import ABC, abstractmethod


# Abstract parent class
class Device(ABC):

    def display_name(self, device_name):
        print("Device Name:", device_name)

    @abstractmethod
    def power_on(self):
        pass


# Child classes
class Light(Device):

    def power_on(self):
        print("Smart Light is now ON")


class Fan(Device):

    def power_on(self):
        print("Smart Fan is now ON")


class Speaker(Device):

    def power_on(self):
        print("Smart Speaker is now ON")


# Making objects
living_light = Light()
room_fan = Fan()
music_speaker = Speaker()


# Turning on each device
living_light.display_name("Living Room Light")
living_light.power_on()

room_fan.display_name("Bedroom Fan")
room_fan.power_on()

music_speaker.display_name("Music Speaker")
music_speaker.power_on()


# Polymorphism using classes with the same method
class Camera:

    def check_status(self):
        print("Security Camera is recording")


class Lock:

    def check_status(self):
        print("Door Lock is secure")


# Store different objects in one list
status_devices = [Camera(), Lock()]

print()
print("===== SMART DEVICE STATUS =====")

for item in status_devices:
    item.check_status()

print("===============================")