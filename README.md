# ByteCart 🛒

**ByteCart** is a Django-based e-commerce website developed as the final project for my Django Backend Technologies training course.

This app demonstrates core backend development skills using Django, with an emphasis on structured templates, model relationships, custom views, and clean URL routing. Each chapter builds on the previous, simulating a real-world development process.

---

## ✅ Chapters Completed

### 📘 Chapter 1 – Project & Base Setup
- Created Django project: `ByteCart`
- Initialized virtual environment and installed Django 5.2
- Set up basic views: `home`, `about`, and `contact`
- Built simple contact form using `forms.Form` with field validation
- Implemented user registration and login with hashed password storage
- Configured `base.html` template and inherited structure for all pages
- Set up static and media directories with:
  - `STATICFILES_DIRS`, `STATIC_ROOT`, `MEDIA_ROOT`
  - `collectstatic` tested and working
- Added Bootstrap to templates for responsive UI

---

### 📗 Chapter 2 – Product App Creation
- Created new Django app: `products`
- Designed `Product` model:
  - Fields: title, slug, description, price, image, featured, active
- Implemented random image upload path with `upload_to` and renaming logic
- Registered `Product` model in admin
- Created custom model manager:
  - `Product.objects.featured()` returns featured items
  - `Product.objects.all()` returns active items

---

### 📕 Chapter 3 – Slugs & URL Routing
- Added unique slugs for products using `SlugField` and `get_absolute_url`
- Connected detail page with slug route: `/products/<slug>/`
- Created product detail view using `DetailView`
- Added fallback `get_object()` with custom error handling for:
  - Missing products
  - Duplicate slugs
- Included `products.urls` in main `urls.py` using `include()`
- Template now uses `reverse()` and `{% url %}` for link generation

---

### 📙 Chapter 4 – Template Design & Refactoring
- Introduced `{% block content %}` and `{% include %}` system for layout control
- Moved product card into `products/snippets/card.html` for reuse
- Enhanced navbar styling:
  - Dynamically highlights current active page
  - Included links to Home, Contact, Products, Login, Register, Logout
- Fixed image display bugs with conditional `{% if instance.image %}`
- Slug-based navigation tested from product list to detail page
- Button and image links now route to the correct detail page
- Improved error messaging and template fallback for missing images or slugs

---

### 🧾 Chapter 5 – Bootstrap Layouts
- Added `container`, `row`, and `col` classes to organize page structure
- Styled product list using Bootstrap grid and card components
- Made product cards responsive across screen sizes
- Improved spacing and layout using `mx-auto`, `text-center`, and `py-` utilities
- Ensured consistent and mobile-friendly UI using Bootstrap 4 conventions

---

## 🧰 Technologies Used
- **Python 3.10**
- **Django 5.2**
- SQLite (default)
- Bootstrap 4 (CDN)
- Custom static files & media file management

---

## 🗂 Folder Structure (Key Parts)

ByteCart/
├── bytecart/ # Core Django project
│ ├── views.py # Home, about, contact, register, login
│ ├── urls.py # Main URL routing
│ └── templates/ # Base and shared templates
│ ├── base/ # Navbar, base.html
│ └── home_page.html # Main homepage
├── products/ # Product app
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/products/
│ ├── list.html
│ ├── detail.html
│ └── snippets/card.html
├── static_my_project/ # Local static files (CSS, JS, images)
├── static_cdn/ # Static and media collected here
│ ├── static_root/
│ └── media_root/
├── db.sqlite3 # Dev database
├── manage.py