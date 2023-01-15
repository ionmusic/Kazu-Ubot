from .. import run_as_module

if not run_as_module:
    from ..exceptions import RunningAsFunctionLibError

    raise RunningAsFunctionLibError(
        "You are running 'Kazu' as a functions lib, not as run module. You can't access this folder.."
    )

from .. import *

CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."

DEVLIST = [
    719195224,  # @xditya
    1322549723,  # @danish_00
    1903729401,  # @its_buddhhu
    1054295664,  # @riizzvbss
    1924219811, # @Banned_3
    883761960,  # @SilenceSpe4ks
    1720836764, # @thisrama
    1803618640, # @onlymeriz
    874946835,  # @vckyaz
    997461844, # @AyiinXd
    1191668125, # @xtsea
    1784606556,  # @greyvbss
    844432220,  # @mrismanaziz
    902478883, # @kenapatagkazu
    5063062493, # @disinikazu
    951454060, # @onlymeriz2
    607067484, # @AyiinXd
]

cmd = CMD_HANDLER
CMD_LIST = {}

DEFAULT = [
    5063062493, # @disinikazu
]

KAZU_IMAGES = [
    f"https://graph.org/file/{_}.jpg"
    for _ in [
        "9b26db2c351d68d71dc1d",
    ]
]

stickers = [

]
