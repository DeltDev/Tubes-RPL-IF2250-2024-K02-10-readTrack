import SplashScreen as ss
import MainMenuScreen as mms
# Function to switch between scenes
def switchToMenu(root):
  mms.create(root)  # Call menu creation function

def switchToSplash(root):
  ss.create(root)