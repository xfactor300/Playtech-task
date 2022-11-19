from bs4 import BeautifulSoup

# read modules.xml file
with open('modules.xml', 'r') as f:
    data = f.read()

modules = BeautifulSoup(data, "xml")
plugins = modules.find_all("plugin")

# find packer plugin and check version
for plugin in plugins:
    if plugin.artifactId.string == "packer" and float(plugin.version.string) < 2:
        plugin.version.string = "2.1"

# find cores tag and remove from tree
cores = modules.find_all("cores")
for core in cores:
    core.decompose()
# save updated file as modules_updated.xml
with open('modules_updated.xml', 'w') as f:
    f.write(Bs_data.prettify())