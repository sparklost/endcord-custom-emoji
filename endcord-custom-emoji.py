import logging
import re

from endcord import formatter

EXT_NAME = "Custom Emoji"
EXT_VERSION = "0.1.1"
EXT_ENDCORD_VERSION = "1.5.0"
EXT_DESCRIPTION = "An extension that adds command to insert any discord emoji or sticker as image url, so it will appear as embed"
EXT_SOURCE = "https://github.com/sparklost/endcord-custom-emoji"
EXT_COMMAND_ASSIST = (
    ("insert_custom_emoji - insert discord emoji as image url in input line", "insert_custom_emoji"),
)
logger = logging.getLogger(__name__)

VS17 = "\U000E0100"
EMOJI_SIZES = [32, 48, 56, 64, 96, 128, 160, 256, 512]
STICKER_SIZES = [32, 64, 128, 160, 256, 512]


class Extension:
    """Main extension class"""

    def __init__(self, app):
        self.app = app
        self.hide_hyperlink = int(app.config.get("ext_custom_hide_hyperlink", True))
        try:
            self.emoji_size = int(app.config.get("ext_custom_emoji_size", 32))
            self.emoji_size = min(EMOJI_SIZES, key=lambda x: abs(x - self.emoji_size))
        except ValueError:
            self.emoji_size = 32
        try:
            self.sticker_size = int(app.config.get("ext_custom_sticker_size", 160))
            self.sticker_size = min(STICKER_SIZES, key=lambda x: abs(x - self.sticker_size))
        except ValueError:
            self.sticker_size = 32
        self.app.premium_override_commands.append("insert_custom_emoji")
        self.run = True


    def on_execute_command(self, command_text, chat_sel, tree_sel):   # noqa
        """Handle commands"""
        if command_text.startswith("insert_custom_emoji"):
            emoji_string = command_text[20:].strip()
            match = re.match(formatter.match_d_emoji, emoji_string)
            if match:
                emoji_name = match.group(2)
                emoji_id = match.group(3)
                if not emoji_id or not emoji_id.isdigit():
                    self.app.update_extra_line("Invalid emoji", color=19)
                    return True
                url = f"https://{self.app.discord.cdn_host}/emojis/{emoji_id}.png?size={self.emoji_size}&quality=lossless&1"
                if self.hide_hyperlink:
                    self.app.insert_into_input_store(f"[{VS17}]({url})")
                else:
                    self.app.insert_into_input_store(f"[{emoji_name}]({url})")
                return True

            match = re.match(formatter.match_sticker_id, emoji_string)
            if match:
                sticker_id = match.group()
                if not sticker_id or not sticker_id[2:-2].isdigit():
                    self.app.update_extra_line("Invalid sticker", color=19)
                    return True
                sticker_id = sticker_id[2:-2]
                url = f"https://{self.app.discord.dyn_cdn_host}/stickers/{sticker_id}.png?size={self.sticker_size}"
                self.app.insert_into_input_store(f"[{VS17}]({url})")
                return True

            self.app.update_extra_line("Invalid emoji", color=19)
            return True
        return False
