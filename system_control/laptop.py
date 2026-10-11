import subprocess
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

def lock_laptop():
    try:
        subprocess.run(
            ["rundll32.exe", "user32.dll,LockWorkStation"],
            check=True
        )
        return "Locking your laptop."
    except Exception as error:
        print(f"Lock error: {error}")
        return "Sorry, I could not lock your laptop."
def get_volume_control():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.EndpointVolume
    return interface

def increase_volume():
    volume = get_volume_control()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(1.0, current + 0.1), None)
    return "Volume increased."


def decrease_volume():
    volume = get_volume_control()
    current = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(max(0.0, current - 0.1), None)
    return "Volume decreased."


def mute_volume():
    get_volume_control().SetMute(1, None)
    return "Volume muted."


def unmute_volume():
    get_volume_control().SetMute(0, None)
    return "Volume unmuted."