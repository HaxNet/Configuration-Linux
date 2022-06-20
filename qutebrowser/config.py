import subprocess
config.load_autoconfig()

# /.config/qutebrowser/config.py
# X configs change options / QB features
config.bind('xc', 'config-cycle tabs.show always never')
config.bind('xx', 'set tabs.show always')
config.bind('xg', 'tab-give')
config.bind('xp', 'spawn ~/.bin/pocketadd {url}')
config.bind('zd', 'download-open')
config.bind('xb', 'config-cycle statusbar.hide')
config.bind('B', 'set-cmd-text -s :bookmark-load')
config.bind('xs', 'config-source')
config.bind('<Alt+Up>', 'tab-prev')
config.bind('<Alt+Down>', 'tab-next')
config.bind('<Alt+Right>', 'tab-give')



# Ctrl shortcuts run scripts / applications
config.bind('<Ctrl-m>', 'spawn --detach mpv --force-window yes {url}')
config.bind('<Ctrl-Shift-p>', 'spawn --userscript qute-lastpass')
config.bind('<Ctrl-r>', 'spawn --userscript readability')
config.bind('<Ctrl-Shift-y>', 'hint links spawn --detach mpv --force-window yes {hint-url}')


# c.? are options set at launch.
c.tabs.favicons.scale = 1
c.tabs.indicator.padding = {"top": 0, "right": 0, "bottom": 0, "left": 0}
c.tabs.position = "top"
#c.tabs.show = "switching"
c.tabs.width = 39
c.content.cookies.accept = 'all'
c.content.geolocation = 'ask'
c.content.webgl = True
# c.downloads.remove_finished = 800
c.auto_save.session = False
c.editor.command = ["urxvtc", "-e", "nvim", "{}"]
c.scrolling.smooth = True


c.url.start_pages = ["https://tekniq.xyz","https://parler.com","https://dev.to/haxnet"]

# search engine shortneners
c.url.searchengines ={
"DEFAULT":"https://bing.com/?q={}",
"Giri": "https://gibiru.com?q={}",
"aur": "https://aur.archlinux.org/packages/?O=0&K={}",
}


#colours
c.colors.completion.fg = "#ffffff"
c.colors.completion.even.bg = "#262626"
c.colors.completion.odd.bg = "#000000"
c.colors.completion.category.fg = "#ffffff"
c.colors.completion.category.bg = "#000000"
c.colors.completion.category.border.top = "#8c8c8c"
c.colors.completion.item.selected.fg = "#ffffff"
c.colors.completion.item.selected.bg = "#cc0000"
c.colors.completion.item.selected.border.top = c.colors.completion.item.selected.bg
c.colors.completion.item.selected.border.bottom = c.colors.completion.category.border.top
c.colors.completion.match.fg = "#f22456"
c.colors.statusbar.insert.bg = "#3a8a16"
c.colors.tabs.odd.fg = "#ffffff"
c.colors.tabs.odd.bg = "#000000"
c.colors.tabs.even.fg = c.colors.tabs.odd.fg
c.colors.tabs.even.bg = c.colors.tabs.odd.bg
c.colors.tabs.selected.odd.bg = "#f22456"
c.colors.tabs.selected.even.bg = c.colors.tabs.selected.odd.bg
c.colors.tabs.bar.bg = "#000000"
c.hints.border = "#000000"
c.colors.hints.fg = "#000000"
c.colors.hints.bg = "#DBFD45"
c.colors.hints.match.fg = "#ffffff"
c.colors.downloads.bar.bg = "#000000"


#config.set("colors.webpage.darkmode.enabled",True)


