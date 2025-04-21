---

# Social Login in Django Using Google & GitHub | Django-allauth

This project demonstrates how to integrate social login functionality into a Django application using Google and GitHub accounts. By using the powerful `django-allauth` package, we enable multiple social authentication providers along with user management features like email login, account verification, and more.

## Overview

Social login allows users to log into your Django application using their existing Google or GitHub accounts, which provides a seamless user experience and saves time by avoiding the need to remember additional passwords.

This project will guide you through setting up social authentication for Google and GitHub with `django-allauth`.

## Prerequisites

Before you begin, ensure the following:

- Python and Django are installed
- A working Django project is set up
- You're using a virtual environment (recommended)
- Familiarity with basic Django concepts

## Steps

### Step 1: Install `django-allauth`

To get started, you first need to install `django-allauth`, which will handle the entire authentication process, including social logins.

Run the following command:

```bash
pip install django-allauth
```

### Step 2: Configure `settings.py`

Once `django-allauth` is installed, you need to add it to your `settings.py` file to enable the authentication providers.

#### 2.1 Add to `INSTALLED_APPS`:

Add the following to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # Required Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',        # Needed for allauth

    # Allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Social providers
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]
```

#### 2.2 Add site configuration:

In `settings.py`, set the `SITE_ID`:

```python
SITE_ID = 1  # This ties your project to the default Django Site object (example.com)
```

#### 2.3 Configure authentication backends:

Configure authentication backends as follows:

```python
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Default
    'allauth.account.auth_backends.AuthenticationBackend',  # Enables allauth
)
```

#### 2.4 Set login redirection URLs:

Add the following settings to specify where users are redirected after login or logout:

```python
SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL = '/'  # After successful login
ACCOUNT_LOGOUT_REDIRECT_URL = '/'  # After logout
```

#### 2.5 Add social login settings:

Add the configuration for Google and GitHub with the `client_id` and `secret` you will obtain from their respective platforms.

```python
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'google_client_id',
            'secret': 'google_secret',
        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'prompt': 'select_account'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': True,
    },
    'github': {
        'APP': {
            'client_id': 'github_client_id',
            'secret': 'github_secret',
        },
        'AUTH_PARAMS': {'prompt': 'select_account'}
    }
}
```

### Step 3: Add URLs

In your project-level `urls.py` file (usually located at `myproject/urls.py`), include the following URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Adds allauth login URLs
]
```

This will provide you with the following login URLs:
- `/accounts/login/`
- `/accounts/logout/`
- `/accounts/signup/`
- `/accounts/google/login/`
- `/accounts/github/login/`

### Step 4: Migrate the Database & Create a Superuser

Run the following commands to apply migrations and create a superuser account:

```bash
python manage.py migrate
python manage.py createsuperuser
```

These migrations will set up all the necessary tables for accounts, social accounts, and sites.

### Step 5: Set Up Google OAuth

To connect your app to Google’s login service, follow these steps:

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Go to **APIs & Services > OAuth Consent Screen**.
4. Choose **External** and fill in the required info (app name, email).
5. Go to **APIs & Services > Credentials**.
6. Click **Create Credentials > OAuth client ID**.
7. Select **Web Application** as the application type.
8. Name the application (e.g., “Django Local”).
9. Under **Authorized redirect URIs**, add the following URI:
   ```
   http://localhost:8000/accounts/google/login/callback/
   ```
10. Click **Create**, and copy the **Client ID** and **Client Secret**.

### Step 6: Set Up GitHub OAuth

To set up GitHub OAuth, follow these steps:

1. Visit [GitHub Developer Settings](https://github.com/settings/developers).
2. Click **OAuth Apps** > **New OAuth App**.
3. Fill in the following:
   - **Application Name**: Choose any name.
   - **Homepage URL**: `http://localhost:8000/`
   - **Authorization callback URL**: `http://localhost:8000/accounts/github/login/callback/`
4. Click **Register Application**, and copy the **Client ID** and **Client Secret**.

### Step 7: Add Social Applications via Admin

Start the server and log in as the superuser:

```bash
python manage.py runserver
```

Then, go to `http://localhost:8000/admin`, log in with the superuser account, and navigate to **Social applications → Add**.

1. **Google Login**:
   - Provider: Google
   - Name: Google Login
   - Client ID & Secret: From Google
   - Sites: Check the one that says `example.com`.

2. **GitHub Login**:
   - Provider: GitHub
   - Client ID & Secret: From GitHub

### Step 8: Test the Login Flow

Finally, test the social login:

1. Visit: `http://localhost:8000/accounts/login/`.
2. You should see login options for Google and GitHub.
3. Click one → Authenticate → Get redirected back to your app.

Congratulations! You’ve successfully integrated Google and GitHub login into your Django application.

---

## References

For further reference, check out the GitHub repository: [Social Login GitHub Repo](https://github.com/Geethika-taashee/social-login).

