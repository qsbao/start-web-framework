

import os
import yaml

applicationPaths = '''example/django-blog/
example/todolist-app/
web-framework/java/springboot
web-framework/nodejs/egg
web-framework/nodejs/express
web-framework/nodejs/hapi
web-framework/nodejs/koa
web-framework/nodejs/midway-koa
web-framework/nodejs/next
web-framework/nodejs/nuxt-ssr
web-framework/php/discuz
web-framework/php/ecshop
web-framework/php/laravel
web-framework/php/metinfo
web-framework/php/thinkphp
web-framework/php/typecho
web-framework/php/whatsns
web-framework/php/wordpress
web-framework/php/zblog
web-framework/python/bottle
web-framework/python/django
web-framework/python/fastapi
web-framework/python/flask
web-framework/python/pyramid
web-framework/python/tornado
web-framework/python/webpy'''

applicationPaths = applicationPaths.split("\n")

for eveApplication in applicationPaths:
    with open(os.path.join(eveApplication, 'publish.yaml')) as f:
        yamlContent = f.read()
    publishyaml = yaml.safe_load(yamlContent)

    applicationName = publishyaml['Name']
    applicationDescription = publishyaml['Description']
    applicationVersion = publishyaml['Version']

    with open(os.path.join(eveApplication, 'readme.md')) as f:
        tempReadmemd = f.read()

    tempReadmemd = tempReadmemd.replace("\`", "`")
    tempReadmemd = tempReadmemd.replace("😼", " :smiley_cat: ")
    tempReadmemd = tempReadmemd.replace("🔥", " :fire: ")

    with open(os.path.join(eveApplication, 'readme.md'), 'w') as f:
        f.write(tempReadmemd)

    with open(os.path.join(eveApplication, 'src/readme.md'), 'w') as f:
        f.write(tempReadmemd)

    versions = applicationVersion.split('.')
    versions[-1] = str(int(versions[-1]) + 1)

    yamlContent = yamlContent.replace(applicationVersion, '.'.join(versions))
    with open(os.path.join(eveApplication, 'publish.yaml'), 'w') as f:
        f.write(yamlContent)


if len(applicationPaths) > 1:
    with open('./update.list', 'w') as f:
        f.write('\n'.join(applicationPaths))
