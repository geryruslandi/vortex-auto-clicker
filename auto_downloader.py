import os
import pyautogui
import time
from pyscreeze import ImageGrab
import traceback

print(os.getcwd())

pyautogui.FAILSAFE = False

# Image file paths
launcher_download_path = "./images/download_launcher.PNG"
website_download_path = "./images/download_website.PNG"
threshold = 0.9

def clickOnImage(location: str, screenshot) -> bool:
    try:
        ui_location = pyautogui.locate(location, screenshot, confidence=threshold)
        print(ui_location)
        if ui_location is not None:
            pyautogui.click(ui_location.left + 5, ui_location.top + 5)
            return True
        return False
    except Exception as e:
        return False

def isCyberpunkGame(screenshot) -> bool:
  try:
    cyberpunk_path = "./images/cyberpunk/cyberpunk_identifier.png"
    ui_location = pyautogui.locate(cyberpunk_path, screenshot, confidence=threshold)
    print("Is cyberpunk game, checking additional cyberpunk button as well")
    return ui_location is not None
  except:
    return False

def checkOnCommonButtons(screenshot) -> bool:
  if clickOnImage(launcher_download_path, screenshot):
    print("Clicked on 'Launcher Download'")
    return True
  elif clickOnImage(website_download_path, screenshot):
    print("Clicked on 'Website Download'")
    return True
  return False

def checkOnCyberpunkButtons(screenshot) -> bool:
  install_staging_path = "./images/cyberpunk/install_staging.png"
  understood_path = "./images/cyberpunk/understood.png"
  continue_path = "./images/cyberpunk/continue.png"

  if clickOnImage(understood_path, screenshot):
    print("Clicked on 'Understood'")
    return True
  elif clickOnImage(continue_path, screenshot):
    print("Clicked on 'Install Staging'")
    return True
  elif clickOnImage(install_staging_path, screenshot):
    print("Clicked on 'Install Staging'")
    return True
  return False

while True:
    try:
        print("Checking for buttons...")
        screenshot = ImageGrab.grab(all_screens=True)

        if checkOnCommonButtons(screenshot):
          time.sleep(2)
          break

        if isCyberpunkGame(screenshot):
          checkOnCyberpunkButtons(screenshot);


    except Exception as e:
      traceback.print_exc()
      print(f"Error in main loop: {e}")

    time.sleep(2)
