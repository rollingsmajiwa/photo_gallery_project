# Photo Gallery Application

## Project Brief

The **Photo Gallery Application** is a modern, responsive web application built with Django and Tailwind CSS. It provides an intuitive interface for photography enthusiasts to explore curated collections, view photo details, filter by tags, and securely manage user accounts.

## Business Rationale

In a visual-centric market, clarity, security, and aesthetics are paramount. This project addresses key digital experience needs:

* **Brand Authority:** A neutral, clean semantic design establishes trust and positions the application as a professional portfolio platform.
* **Data Management:** Structured SQLite persistence ensures user registrations, contact messages, and media assets are safely managed.
* **Access Control:** Role-based access ensures public discovery on the home page while keeping full high-resolution galleries protected behind user authentication.

## Technologies used

* **Python 3.x / Django:** Robust back-end framework powering routing, view logic, and database ORM.
* **HTML5 & Tailwind CSS:** Semantic markup combined with utility-first CSS using a neutral color palette (slate, black, white) for modern responsive styling.
* **Pillow:** Image processing library handling media file uploads.
* **Git/GitHub:** Version control and feature-based development workflow.

## Accessibility features

* **Semantic HTML:** Utilizes `<header>`, `<main>`, `<section>`, `<nav>`, and `<footer>` tags for seamless screen reader navigation.
* **Form Field Labels:** Explicit `for` attributes paired with input `id` specifications across contact, registration, and authentication forms.
* **High Contrast Elements:** Dark slate buttons and clean typography ensure high legibility against crisp backgrounds.

## Product features

The application delivers core functionality across distinct module tiers:

* **Landing Experience:** Public homepage featuring a hero showcase banner and featured preview grids.
* **Protected Gallery:** High-resolution photo grid accessible strictly to authenticated accounts.
* **User Authentication:** Built-in account creation, login verification, and secure session management.
* **Contact Management:** Direct inquiry submissions saved directly into database models.

## Git workflow

* **Fork the Repository:** Create your own copy of the project to work on.
* **Create a Feature Branch:**

```bash
git checkout -b YourFeatureName
Commit Your Changes

Push to branch:

Bash
git push origin feature/YourFeatureName
Open a Pull Request (PR): Describe your changes clearly and link related issues.
```

## Set up instructions
a. Clone this repository on your local machine:

```Bash
git clone [https://github.com/rollingsmajiwa/PHOTO_GALLERY_APP.git](https://github.com/rollingsmajiwa/PHOTO_GALLERY_APP.git)
cd PHOTO_GALLERY_APP
```
b. Create and activate a virtual environment, then install dependencies:

```Bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install django pillow
```
c. Apply migrations and start the local development server:

```Bash
python manage.py migrate
python manage.py runserver
```


## Author
Rollings Majiwa

GitHub: [https://github.com/rollingsmajiwa](https://github.com/rollingsmajiwa)

Email: [rollingsmajiwa@gmail.com](rollingsmajiwa@gmail.com)

## Get started
Interested in the code behind Photo Gallery Application? You can reach me directly via my profile or open an issue for collaboration. Visit my GitHub profile.