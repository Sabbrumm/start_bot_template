from configmagic import ConfigMagic
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(ROOT_DIR, 'config.ini')
locale_path = os.path.join(ROOT_DIR, 'locale.ini')

vConfig = ConfigMagic(config_path)
config = vConfig.parse()

vLocale = ConfigMagic(locale_path)
loc = vLocale.parse()
