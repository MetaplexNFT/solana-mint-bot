import os
import json
import magiceden
import monkelabs

# return wallet config
def getConfig():
  configFile = open("config.json", 'r')
  return list(json.load(configFile).values())

# setup config
config = getConfig()

isWindows = True if os.name == 'nt' else False

if "magiceden.io" in config[0]:
  print("Minting on Magiceden")
  magiceden.mint(config, isWindows)

elif "monkelabs.io" in config[0]:
  print("Minting on Monkelabs")
  monkelabs.mint(config, isWindows)

else:
  print("Put a Magiceden or Monkelabs link on config")

