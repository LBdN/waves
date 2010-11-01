import cocos
import os
import configobj_ext
import tiled2cocos

DEFAULT_PATH = "./config.ini"
DEFAULT_SPEC = "./config_spec.ini"

def app_path(rel_path):
    application_path = os.path.dirname(__file__)
    return os.path.join(application_path, rel_path)

def load_config():
    path   = app_path(DEFAULT_PATH)
    spec   = app_path(DEFAULT_SPEC)
    config = configobj_ext.read_config(path, configspec=spec)
    return config

def prepare(config):
    cocos.director.director.init(width=config.Window.width, height=config.Window.height)

class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super( HelloWorld, self ).__init__()

        label = cocos.text.Label('Gros bisous Even'.upper(),
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center')

        label.position = 320,240
        self.add( label )

if __name__ == "__main__":
    config = load_config()
    prepare(config)
    map_layer   = tiled2cocos.load_map(config.Ressources.map3)
    map_layer.set_view(0, 0, config.Window.width, config.Window.height)
    #map_layer.x = config.Window.width / 2.0
    #map_layer.y = config.Window.height / 2.0
    for c in map_layer.get_children():
        print c
        c.do(cocos.actions.RotateBy( 360, duration=2 ))
    hello_layer = HelloWorld ()
    main_scene  = cocos.scene.Scene (*[map_layer, hello_layer])
    hello_layer.do( cocos.actions.RotateBy( 720, duration=5 ))

    cocos.director.director.run (main_scene)
