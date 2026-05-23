import os
import django
import pydoc

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MY_SITE.settings')
django.setup()


# Archivos HTML que se regenerarán
files = [
    "blog.models.html",
    "blog.views.html"
]

# Borrar HTML antiguos
for file in files:
    if os.path.exists(file):
        os.remove(file)

# Generar documentación
pydoc.writedoc('blog.models')
pydoc.writedoc('blog.views')

# HTML generados
files = [
    "blog.models.html",
    "blog.views.html"
]

# Añadir CSS automáticamente
for file in files:

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace(
        "</head>",
        '<link rel="stylesheet" type="text/css" href="style.css">\n</head>'
    )

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Documentació generada correctament")