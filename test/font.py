import matplotlib.font_manager

fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext='ttf')
print(fonts)

font_names = [f.name for f in matplotlib.font_manager.fontManager.ttflist]
print(font_names)
