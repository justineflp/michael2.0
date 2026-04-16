# Lodgio
A comprehensive platform to manage reservations, listings, communications, and customer interactions dynamically for lodging businesses.

---

## Group Members

| Name | Assigned App | Scope |
| ---- | ------------ | ----- |
| gmmichael05-lang (Group Leader) | `accounts` | User & profile authentication |
| gmmichael05-lang (Group Leader) | `properties` | Management of lodging properties, availability blocks, and active bookings |
| Kirsten Baldon | `communications` | System messaging, user dispute tickets, and identity verification logic |
| Ken | `discovery` | User search histories, wishlist saves, and listing approval processes |
| intra-glitch (Allan) | `marketing` | Promotional coupons, discount implementations, and guest reviews |
| Reserved (TBD) | `finances` | Administrative logic for payment and host payouts (Placeholder Setup) |

---

## Project Structure

```
michael2.0/
├── lodgio/                    # Core project configurations
│   ├── settings.py            # Django settings (uses SQLite3)
│   ├── urls.py                # Root URL configuration pointing to the 6 apps
├── accounts/                  # User Management & Dashboard
├── properties/                # Listing, CalendarBlock, Booking
├── communications/            # IdentityDocument, Message, ReportTicket
├── discovery/                 # SearchLog, ListingApproval, Wishlist
├── marketing/                 # Coupon, CouponUsage, Review
├── finances/                  # PriceAdjustment, Payment, HostPayout, AdminLog (Skeletons)
├── db.sqlite3                 # Pre-populated local database
├── manage.py
└── README.md
```

---

## Requirements

- Python 3.10+
- Django 5.0+ (or as specified in your environment)
- **Note:** The included `db.sqlite3` file is pre-configured and pre-migrated to save you from running MySQL database migrations. You can run the application directly out-of-the-box.

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/justineflp/michael2.0.git
cd michael2.0
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the development server
Because a pre-migrated `db.sqlite3` is shipped with this branch, you **do not need to migrate**.
```bash
python manage.py runserver
```

### 5. Open in browser
```
http://127.0.0.1:8000/
```

You will load into the index login page. 

### 6. Login as an Admin
To view the structure and routing natively, you can use the superuser account embedded in the repository:
- **Email:** `admin@lodgio.com`
- **Password:** `adminpassword`

---

## URL Structure

| URL | Description |
|-----|-------------|
| `/` | Index — Landing and Login |
| `/accounts/` | Accounts Dashboard |
| `/properties/` | Properties & Bookings logic |
| `/communications/` | Communications logic |
| `/discovery/` | Discovery & Features logic |
| `/marketing/` | Marketing & Engagements logic |
| `/finances/` | Finances logic (Under Construction) |
| `/admin/` | Django Built-in Admin panel (superusers only) |

---

## Notes

- The custom `User` model (`accounts.User`) requires an explicit `email` rather than a standard `username` for logging in.
- To use MySQL instead of the native SQLite3 database shipped with the repo, open `lodgio/settings.py` and replace the `DATABASES` dictionary with `django.db.backends.mysql` along with your local root credentials.
