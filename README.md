# 🛒 ByteCart – Django E-commerce App

**ByteCart** is a full-stack e-commerce website built with **Django 5.2**, developed as the final project for my *Django Backend Technologies* training course.

It simulates a real-world development process with clean models, user authentication, cart and checkout flows, and reusable Django components. The app supports both guest and registered user checkout using session-based logic.

---

## ✅ Chapters Completed

### 📘 Chapter 1 – Project & Base Setup
- Created Django project: `ByteCart`
- Set up virtual environment and installed Django 5.2
- Created `home`, `contact`, and user authentication views
- Configured template inheritance (`base.html`)
- Set up `static_my_project`, `static_cdn`, and Bootstrap 4 styling

---

### 📗 Chapter 2 – Product App Creation
- Created `products` app
- Defined `Product` model with: `title`, `slug`, `description`, `price`, `image`, `featured`, `active`
- Created image renaming and upload path logic
- Added custom `ProductManager` with `.all()` and `.featured()` methods

---

### 📕 Chapter 3 – Slugs & URL Routing
- Implemented auto-generated slugs with `SlugField` and `unique_slug_generator`
- Set up `get_absolute_url()` and proper URL routing using `{% url %}`
- Fallback slug creation logic for uniqueness

---

### 📙 Chapter 4 – Template Refactoring & Snippets
- Modularized templates using `snippets/card.html`, `snippets/navbar.html`
- Improved product cards using Bootstrap grid and responsive layout
- Active navbar highlighting using Django template tags

---

### 🧾 Chapter 5 – Bootstrap Layouts
- Built responsive product grids using Bootstrap 4
- Structured consistent layout across base and sub-templates
- Fixed product image scaling and card layouts

---

### 🔍 Chapter 6 – Search System
- Created `search` app and connected to `/search/`
- Implemented `SearchProductView` using `ListView`
- Used `Q()` objects for flexible field filtering (`title`, `description`, `price`)
- Built reusable search form and integrated it in the navbar
- Added `Tag` model to enhance product filtering

---

### 🛒 Chapter 7 – Cart System (Session-Based)
- Created `carts` app with custom `CartManager.new_or_get()`
- Defined `Cart` model with `ManyToManyField` to `Product`
- Session-based cart logic with `session['cart_id']`
- Built `cart_home` and `cart_update` views
- Added `m2m_changed` and `pre_save` signals for subtotal/total updates
- Created reusable cart update form in `snippets/update-cart.html`
- Integrated cart functionality into product detail pages

---

### 📦 Chapter 8 – Checkout Flow (Billing, Addresses, Orders)
- Created `billing` app with `BillingProfile` model linked to `User` or guest session
- Created `orders` app with `Order` model:
  - `billing_profile`, `cart`, `status`, `shipping_address`, `billing_address`, `order_total`
- Added `OrderManager.new_or_get()` for cart-order lifecycle
- Connected `pre_save` signal for `order_id` and active flag switching
- Connected `post_save` signal to sync cart and order totals
- Created `addresses` app with reusable `AddressForm`
- Address selection based on `address_type` (`shipping` / `billing`)
- Implemented full address flow:
  - Guest checkout via email (stored in session)
  - Reuse addresses if already in session
  - Address creation form with redirect support via `?next=`
- Ensured secure redirecting using `url_has_allowed_host_and_scheme()`

---

## 🧰 Technologies Used

- **Python 3.10**
- **Django 5.2**
- **SQLite 3** (default dev DB)
- **Bootstrap 4** (CDN)
- **Django sessions**
- Custom `BillingProfile`, `Order`, `Address`, and `Cart` models

---

## 🗂 Folder Structure (Key Parts)

```plaintext
ByteCart/
├── bytecart/               # Project config + base views
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── base.html
├── accounts/               # Login, registration, guest logic
├── addresses/              # Shipping / billing address logic
├── billing/                # BillingProfile logic per user/guest
├── carts/                  # Session-based cart
│   ├── models.py
│   ├── views.py
│   └── templates/carts/cart_home.html
├── orders/                 # Order lifecycle
│   ├── models.py
│   ├── signals.py
│   └── views.py
├── products/               # Product list, detail, tagging
│   ├── models.py
│   ├── views.py
│   └── templates/products/
├── search/                 # Basic search with filters
├── static_my_project/      # Local static files
├── static_cdn/             # Collected static/media files
├── db.sqlite3
└── manage.py
