import util
from catppuccin import Flavour


def cat(name):
    return lambda opt: getattr(opt['flavour'], name).hex


def create_mapping(accent):
    mapping = {
        '000000': cat('crust'),
        '232323': cat('crust'),
        'ffffff': cat('text'),

        # text
        'e6e6e6': cat('text'),
        'd9d9d9': cat('subtext1'),
        '999999': cat('subtext0'),
        '888888': cat('subtext0'),
        '8383838': cat('subtext0'),
        'dddddd': cat('subtext1'),
        'cccccc': cat('subtext1'),
        'c3c3c3': cat('subtext1'),
        'eeeeee': cat('subtext1'),
        '989898': cat('subtext0'),
        'a6a6a6': cat('subtext0'),

        # UI colors
        '181818': cat('crust'),
        '1d1d1d': cat('mantle'),

        'ff3352': cat('red'),  # x axis
        '8bdc00': cat('green'),  # y axis
        '2890ff': cat('blue'),  # z axis


        '3d3d3d': cat('base'),  # 3D viewer gradient high
        '303030': cat('mantle'),  # 3D viewer gradient low
        '545454': cat('surface0'),  # gridlines

        '333333': cat('base'),
        '262626': cat('mantle'),

        '2b2b2b': cat('base'),
        '282828': cat('mantle'),

        '4772B3': accent,
        '4772b3': accent,

        # Icon colors
        '00d4a3': cat('green'),
        '74a2ff': cat('blue'),
        'cc6670': cat('red'),

        # Python terminal colors
        '71A8FF': cat('blue'),
        'f2f2f2': cat('text'),
        '95d600': cat('green'),
        'ff4d84': cat('maroon'),
        'ff0000': cat('red'),
    }
    return mapping


# Only the darker ones look OK
supported_accent_colors = ['mauve', 'red', 'green', 'sapphire']

for name, flavour in (
    ('Latte', Flavour.latte()),
    ('Frappe', Flavour.frappe()),
    ('Macchiato', Flavour.macchiato()),
    ('Mocha', Flavour.mocha())
):
    opt = {
        'flavour': flavour
    }
    for accent in supported_accent_colors:
        mapping = create_mapping(accent=cat(accent))
        util.map_colors(input_file="DefaultDarkTheme.xml",
                        opt=opt,
                        mapping=mapping,
                        output_file_name=f'../themes/Catppuccin {name} {accent.capitalize()}.xml')
