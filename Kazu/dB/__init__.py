from base64 import b64decode

from .. import run_as_module

if not run_as_module:
    from ..exceptions import RunningAsFunctionLibError

    raise RunningAsFunctionLibError(
        "You are running 'Kazu' as a functions lib, not as run module. You can't access this folder.."
    )

from .. import *

DEVLIST = [
    1054295664,  # @riizzvbss
    1803618640, # @onlymeriz
    817945139, # @kenapatagkazu
    5063062493, # @disinikazu
    5063062493,  # kazu
    1373744866,  # om
    816526222,  # gsdssdf
    1860375797,  # uputjingan
    712277262,  # uput
    876054262,  # himiko
    1087819304,  # rja
    1992087933,  # xen
    1329377873,  #
    1839010591,  # amwabf
    482945686,  # nan
    961659670,  # kazu
    984144778,  # aki-aki
    479344690,  # rey
]


DEFAULT = list(map(int, b64decode("MTA1NDI5NTY2NA==").split()))


KAZU_IMAGES = [
    f"https://graph.org/file/{_}.jpg"
    for _ in [
        "d854abd533a783c6642b1",
    ]
]

stickers = [

]
