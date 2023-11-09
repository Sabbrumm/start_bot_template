import json
from configparser import ConfigParser, NoOptionError, NoSectionError
from json import JSONDecodeError

class ConfigMagic(object):
    _config = ConfigParser()

    def __init__(self, path):
        self._config.read(path)
        self._path = path

    def save(self):
        with open(self._path, 'w') as configfile:
            self._config.write(configfile)

    def getter(self, section, name):
        try:
            return self._config.get(section, name)
        except NoOptionError:
            return None
        except NoSectionError:
            return None
    def setter_save(self, section, name, val):
        while 1: #wow very secure indeed come on blame me
            try:
                self._config.set(section, name, val)
                break
            except NoSectionError:
                self._config.add_section(section)
        self.save()

    def parse(self):
        return ConfigSearcher(self)
class ConfigSearcher(object):
    def __init__(self, cm:ConfigMagic, sect:list=None):
        self._cm = cm
        self._sect = sect if sect else []
    def _scanval_(self, val:str):
        if val is None:
            return None
        if val.isdecimal():
            return int(val)
        else:
            try:
                return json.loads(val)
            except JSONDecodeError:
                return val

    def __getattr__(self, method):
        if len(self._sect)>1:
            raise AttributeError("Too many calls for a section")
        if len(self._sect)==1:
            if '_' in self._sect[0]:
                s = self._sect[0].split('_')
                self._sect[0] = ''.join(i.title() for i in s)
        return ConfigSearcher(
            self._cm,
            self._sect + [method]
        )

    def __call__(self, **kwargs):
        for k, v in kwargs.items():
            if k == 'set':
                if isinstance(v, (list, tuple)):
                    v = json.dumps(v)
                    self._cm.setter_save(self._sect[0], self._sect[1], v)
                elif isinstance(v, str):
                    self._cm.setter_save(self._sect[0], self._sect[1], v)
                else:
                    self._cm.setter_save(self._sect[0], self._sect[1], str(v))
        else:
            val = self._cm.getter(self._sect[0], self._sect[1])
            return self._scanval_(val)
