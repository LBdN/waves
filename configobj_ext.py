from configobj  import ConfigObj, Section, flatten_errors
from validate import Validator     

def read_config(path, configspec=None):
    monkey_patch_section(Section) # dark stuff
    config    = ConfigObj(path, configspec = configspec)
    validator = Validator()
    result    = config.validate(validator)
    assert result == True
    return config

def pp_errors(config, errors):
    for (section_list, key, _) in flatten_errors(config, errors):
        if key is not None:
            print 'The "%s" key in the section "%s" failed validation' % (key, ', '.join(section_list))
        else:
            print 'The following section was missing:%s ' % ', '.join(section_list)

def monkey_patch_section(cls):
    def getattr(self, key):
        return self[key] if key in self else super(cls, self).__getattr__(self, key)
    cls.__getattr__ = getattr
    return cls
