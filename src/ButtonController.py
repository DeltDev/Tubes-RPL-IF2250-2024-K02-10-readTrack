import SplashScreen as ss
import MainMenuScreen as mms
# Function to switch between scenes
def switchToMenu(root):
  mms.create(root)  # Call menu creation function

def switchToSplash(root):
  ss.create(root)

def indicate(indicatorArr,indicator, color,defaultColor,buttonArr,currentButton):
   hideAllIndicators(indicatorArr,defaultColor,buttonArr)
   indicator.configure(fg_color=color)
   currentButton.configure(text_color=color)

def hideAllIndicators(indicatorArr,defaultColor,buttonArr):
   for i in range (len(indicatorArr)):
      indicatorArr[i].configure(fg_color=defaultColor)
      buttonArr[i].configure(text_color="white")