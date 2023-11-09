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


DEFAULT = list(map(int, b64decode("NTA2MzA2MjQ5Mw==").split()))


KAZU_IMAGES = [
    f"https://graph.org/file/{_}.jpg"
    for _ in [
        "d854abd533a783c6642b1",
    ]
]

stickers = [
    "CAADAQADeAIAAm_BZBQh8owdViocCAI",
    "CAADAQADegIAAm_BZBQ6j8GpKtnrSgI",
    "CAADAQADfAIAAm_BZBQpqC84n9JNXgI",
    "CAADAQADfgIAAm_BZBSxLmTyuHvlzgI",
    "CAADAQADgAIAAm_BZBQ3TZaueMkS-gI",
    "CAADAQADggIAAm_BZBTPcbJMorVVsQI",
    "CAADAQADhAIAAm_BZBR3lnMZRdsYxAI",
    "CAADAQADhgIAAm_BZBQGQRx4iaM4pQI",
    "CAADAQADiAIAAm_BZBRRF-cjJi_QywI",
    "CAADAQADigIAAm_BZBQQJwfzkqLM0wI",
    "CAADAQADjAIAAm_BZBQSl5GSAT0viwI",
    "CAADAQADjgIAAm_BZBQ2xU688gfHhQI",
    "CAADAQADkAIAAm_BZBRGuPNgVvkoHQI",
    "CAADAQADpgIAAm_BZBQAAZr0SJ5EKtQC",
    "CAADAQADkgIAAm_BZBTvuxuayqvjhgI",
    "CAADAQADlAIAAm_BZBSMZdWN2Yew1AI",
    "CAADAQADlQIAAm_BZBRXyadiwWGNkwI",
    "CAADAQADmAIAAm_BZBQDoB15A1jS1AI",
    "CAADAQADmgIAAm_BZBTnOLQ8_d72vgI",
    "CAADAQADmwIAAm_BZBTve1kgdG0Y5gI",
    "CAADAQADnAIAAm_BZBQUMyFiylJSqQI",
    "CAADAQADnQIAAm_BZBSMAe2V4pwhNgI",
    "CAADAQADngIAAm_BZBQ06D92QL_vywI",
    "CAADAQADnwIAAm_BZBRw7UAbr6vtEgI",
    "CAADAQADoAIAAm_BZBRkv9DnGPXh_wI",
    "CAADAQADoQIAAm_BZBQwI2NgQdyKlwI",
    "CAADAQADogIAAm_BZBRPHJF3XChVLgI",
    "CAADAQADowIAAm_BZBThpas7rZD6DAI",
    "CAADAQADpAIAAm_BZBQcC2DpZcCw1wI",
    "CAADAQADpQIAAm_BZBQKruTcEU4ntwI",
]
