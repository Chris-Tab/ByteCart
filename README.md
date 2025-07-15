# ByteCart 🛒

**ByteCart** is a Django-based e-commerce website developed as the final project for my Django Backend Technologies training course.

This app demonstrates core backend development skills using Django, with an emphasis on structured templates, model relationships, custom views, and clean URL routing. Each chapter builds on the previous, simulating a real-world development process.

---

## ✅ Chapters Completed

### 📘 Chapter 1 – Project & Base Setup
- Created Django project: `ByteCart`
- Set up virtual environment and installed Django 5.2
- Built home, contact, and user auth views
- Configured template inheritance (`base.html`)
- Added static/media directories and Bootstrap 4 styling

---

### 📗 Chapter 2 – Product App Creation
- Created `products` app
- Defined `Product` model with fields: title, slug, description, price, image, featured, active
- Registered product model in admin
- Implemented image renaming logic
- Custom model manager with `.featured()` and `.all()`

---

### 📕 Chapter 3 – Slugs & URL Routing
- Implemented unique slugs using `SlugField` and `unique_slug_generator`
- Product detail view with fallback logic
- Used `get_absolute_url()` and `{% url %}` for routing

---

### 📙 Chapter 4 – Template Design & Refactoring
- Moved repeated product card HTML to `snippets/card.html`
- Dynamic navbar with active link highlighting
- Clean routing between product list and detail

---

### 🧾 Chapter 5 – Bootstrap Layouts
- Responsive grid system for product list
- Used Bootstrap cards, spacing utilities, and layout helpers
- Fixed image layout bugs and mobile responsiveness

---

### 🔍 Chapter 6 – Search Component
- Created `search` app and wired it to `/search/`
- Built `SearchProductView` using `ListView`
- Displayed query dynamically in results page
- Created standalone search form and included it in the navbar
- Used `Q()` lookups for flexible search (`title`, `description`, `price`)
- Implemented dynamic layout for search results
- Created `Tag` model and `Product.objects.search()` with `.active()` and `.distinct()`
- Integrated search with query param logic (`?q=...`)
- Fixed form, URL, and field issues with `name="q"`, proper action, and Bootstrap layout

---

## 🧰 Technologies Used
- **Python 3.10**
- **Django 5.2**
- SQLite (default)
- Bootstrap 4 (CDN)
- Custom static/media file management

---

## 🗂 Folder Structure (Key Parts)

ByteCart/
├── bytecart/
│ ├── views.py
│ ├── urls.py
│ └── templates/
│ ├── base/
│ └── home_page.html
├── products/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── templates/products/
│ ├── list.html
│ ├── detail.html
│ └── snippets/card.html
├── search/
│ ├── views.py
│ ├── urls.py
│ └── templates/search/
│ ├── view.html
│ └── snippets/search-form.html
├── static_my_project/
├── static_cdn/
│ ├── static_root/
│ └── media_root/
├── db.sqlite3
├── manage.py