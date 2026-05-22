import os 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MY_SITE.settings')
django.setup()

import pydoc
pydoc.writedoc('blog.models')
pydoc.writedoc('blog.views')