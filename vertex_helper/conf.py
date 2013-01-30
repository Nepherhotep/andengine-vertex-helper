###############################################################################
# Encoding: UTF-8                                                             #
# Author: Alexey Zankevich <alex.zankevich@gmail.com>                         #                                      
# Copyright: (c) 2010 Alexei Zankevich <alex.zankevich@gmail.com>             #                                      
# Licence: BSD                                                                #
############################################################################### 
import os
import pickle



BASE_DIR = os.path.abspath('.')
CONF_FILE = '.avhelper.conf'
CONF_PATH = os.path.join(os.path.expanduser('~'), CONF_FILE)


class Conf(dict):
    def save(self):
        with open(CONF_PATH, 'w') as f:
            pickle.dump(_conf, f);


_conf = Conf()
_conf['pattern'] = "new Vector2(%+.5ff*width, %+.5ff*height),"
_conf['sprites_dir'] = os.path.join(BASE_DIR, 'sprites')
_conf['x_max'] = 360
_conf['y_max'] = 240
_conf['sort_clockwise'] = True
_conf['inverted_y'] = True


def load():
    try:
        with open(CONF_PATH) as f:
            _conf.update(pickle.load(f))
            
    except Exception as e:
        pass
    return _conf
