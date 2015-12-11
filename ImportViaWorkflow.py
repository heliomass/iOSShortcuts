# https://github.com/heliomass/iOSWorkflows
import clipboard
import editor
import urllib
import console
url = clipboard.get()
filename = url.split('/')[-1]
console.hud_alert('Downloading and creating ' + filename)
f = urllib.urlopen(url)
content = f.read()
f.close()
editor.make_new_file(filename, content)
editor.open_file(filename)
