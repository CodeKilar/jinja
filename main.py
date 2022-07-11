import jinja2


sPath = "./"
loader = jinja2.FileSystemLoader(sPath)
JinjaEnv = jinja2.Environment(loader=loader)

dData = {}
dData["DataList"] = [1, 2, 3, 4]

sTemplate = "base.jinja"
oTemplate = JinjaEnv.get_template(sTemplate)
content = oTemplate.render(dData)
print(content)
