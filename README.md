# ByteCart 🛒

**ByteCart** is a Django-based e-commerce website developed as the final project for my Django Backend Technologies training course.

It is built with clean code structure, real-world features, and production-ready practices — showcasing a strong grasp of Django’s core concepts including URL routing, templates, authentication, and static file management.

---

## 💻 Features Implemented (Chapter 1 Complete ✅)

- Django project setup with virtual environment
- Custom homepage, about, and contact pages using Django views and templates
- Contact form using Django’s `forms.Form`, with validation and cleaned data
- User registration with input validation and secure password hashing
- User login and session-based authentication
- Template folder configured with settings and dynamic context passed via views
- Static and media file folders structured and configured:
  - `STATICFILES_DIRS`, `STATIC_ROOT`, `MEDIA_ROOT`
  - Successfully tested `collectstatic` and file organization
- Bootstrap-compatible base template (ready for layout structure)
- Basic error handling and debug troubleshooting


## 🧱 Features Implemented (Chapter 2 & 3 Complete ✅)

- Created new Django app: `products`
- Defined `Product` model with title, description, price, image, featured, and active flags
- Image upload functionality with random renaming and dynamic storage path
- Custom model manager with `featured()` and `active()` querysets
- `SlugField` support for SEO-friendly URLs, auto-generated with a unique slug generator
- Detail page accessible by slug: `/products/<slug>/`
- Template updates to safely handle products with or without images
- Cleaned URL structure using `products/urls.py` and included in root via `include()`
- Product detail URLs generated using Django’s `reverse()` inside `get_absolute_url`
- Static image fallback for missing product images


---

## 🚀 Technologies Used

- **Python 3.10**
- **Django 5.2**
- HTML5 / CSS3 (with support for Bootstrap)
- SQLite (default development database)

---

## 📁 Folder Structure (Key Elements)

```plaintext
ByteCart/
├── bytecart/               # Django project core
│   ├── views.py            # Main views: home, about, contact, login, register
│   ├── urls.py             # Route handling
│   └── templates/          # HTML templates (organized by section)
├── static_my_project/      # Custom static files (CSS, JS, images)
├── static_cdn/             # Collectstatic destination
│   ├── static_root/
│   └── media_root/
├── manage.py
