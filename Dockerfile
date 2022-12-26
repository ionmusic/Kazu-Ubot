# Ayra - UserBot
# Copyright (C) 2021-2022 Riizzvbss
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

FROM theteamultroid/ultroid:main

# set timezone
ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/ionmusic"

# start the bot.
CMD ["bash", "startup"]
