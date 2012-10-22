import os
import shutil

from fabric.api import task
from jinja2 import Environment, FileSystemLoader

import settings


env = Environment(autoescape=True, loader=FileSystemLoader('./'))


@task
def build():
    shutil.rmtree(settings.BUILD_DIR, True)
    os.mkdir(settings.BUILD_DIR)

    template = env.get_template(settings.INDEX_FILE)
    with open(os.path.join(settings.BUILD_DIR, 'index.html'), 'w') as f:
        f.write(template.render())

    shutil.copytree(settings.ASSET_DIR,
                    os.path.join(settings.BUILD_DIR, settings.ASSET_DIR))
