# Blog Django

## Introducció

Aquest projecte és una aplicació web desenvolupada amb Django dins del mòdul de Programació.

L’aplicació consisteix en un blog on es poden visualitzar diferents publicacions, consultar informació dels autors i navegar entre etiquetes relacionades amb els posts.

L’objectiu principal del projecte ha estat practicar el funcionament bàsic de Django treballant amb:

- Models
- Vistes
- URLs
- Plantilles HTML
- Relacions entre taules
- Bootstrap i CSS

També s’ha treballat amb GitHub i documentació automàtica amb Pydoc.

---

<<<<<<< HEAD
=======
# Documentació Pydoc

La documentació automàtica del projecte es pot consultar aquí:

https://zakariabourk.github.io/Django/

>>>>>>> 07b7491e74480a154c747eb1cca11d722d319569

# Instal·lació ràpida

## Clonar el repositori

```bash
git clone https://github.com/ZakariaBourk/Django.git
```

## Entrar a la carpeta del projecte

```bash
cd Django
```

## Crear un entorn virtual

```bash
python -m venv venv
```

## Activar l’entorn virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux o Mac

```bash
source venv/bin/activate
```

## Instal·lar dependències

```bash
pip install -r requirements.txt
```

## Executar migracions

```bash
python manage.py migrate
```

---

# Execució del projecte

Per executar el servidor localment:

```bash
python manage.py runserver
```

Després es podrà accedir al projecte des del navegador amb la següent URL:

```text
http://127.0.0.1:8000/
```

---

# Estructura del projecte

- `blog/`
  - `migrations/`
  - `static/`
  - `templates/blog/`
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `tests.py`
  - `urls.py`
  - `views.py`

- `MY_SITE/`
  - `asgi.py`
  - `settings.py`
  - `urls.py`
  - `wsgi.py`

- `db.sqlite3`
- `manage.py`
- `README.md`

---

# Funcionalitats principals

- Visualització de posts.
- Pàgina principal amb posts destacats.
- Sistema d’autors.
- Sistema d’etiquetes.
- Detall individual de cada post.
- Navegació entre pàgines amb Django URLs.
- Gestió de dades amb models Django.

---

# Tecnologies utilitzades

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite
- GitHub
- Pydoc

---

---

# Autor

Zakaria EL Bourkhissi
