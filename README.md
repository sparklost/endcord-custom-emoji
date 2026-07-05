# endcord-custom-emoji
An extension for [endcord](https://github.com/sparklost/endcord) discord TUI client, that adds command to insert any discord emoji or sticker as image url, so it will appear as embed.  
Adds command `insert_custom_emoji [emoji/sticker]`. it expects `<:emoji_name:en=moji_id>` or `<;sticker_id;>` as argument.  
They can be inserted with emoji/sticker assist.  
Assist is overriden to show all emoji and stickers only for this command.

## Installing
See [official extensions documentation](https://github.com/sparklost/endcord/blob/main/extensions.md#installing-extensions) for installing instructions.
Available options:
- Git clone into `Extensions` directory located in endcord config directory.
- Run `endcord -i https://github.com/sparklost/endcord-custom-emoji`
- Or use endcord client-side command `install_extension sparklost/endcord-custom-emoji`

## Configuration
All extension options are under `[main]` section in endcord config. This extension options are always prefixed with `ext_custom_emoji_`.  

### Settings options
- `ext_custom_hide_hyperlink = True`  
    Hide hyperlink by putting invisible variation selector 17 character instead of emoji name.
- `ext_custom_emoji_size = 32`  
    Image size for sent emoji.
- `ext_custom_sticker_size = 160`  
    Image size for sent stickers.


## Disclaimer
> [!WARNING]
> Using third-party client is against Discord's Terms of Service and may cause your account to be banned!  
> **Use endcord and/or this extension at your own risk!**  
> If this extension is modified, it may be used for harmful or unintended purposes.  
> **The developer is not responsible for any misuse or for actions taken by users.**  
