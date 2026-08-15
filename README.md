# Online Tutoring Platform

A small Django MVP for **CSE 3206 - Software Engineering Sessional, Lab 2**.

## Lab Alignment

- Project: **Online Tutoring Platform**
- Group: **Group #07, Section C (1st 30)**
- Selected process model: **Agile Scrum**
- MVP focus: authentication, tutor profiles/search, tutoring requests, dashboards, request-status management
- Collaboration: individual feature branches, meaningful commits, Pull Requests, code review, merge to `main`

## Team Members

| Name | Student ID | GitHub | Role | Main contribution |
|---|---:|---|---|---|
| Abdullah Al Kafi | 2203139 | `Kafi2611` | Scrum Master + Developer | Authentication, roles, access control |
| Sadaf Rahman | 2203140 | `sadaf532` | Product Owner Representative + Developer | Tutor profile and tutor discovery |
| Sakila Akter | 2203141 | `SakilaAkter` | Developer | Tutoring requests and dashboards |

## Tech Stack

- Python
- Django
- SQLite
- HTML/CSS
- Git and GitHub

## Quick Start

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
cd src
python manage.py makemigrations accounts tutors bookings
python manage.py migrate
python manage.py seed_demo
python manage.py test
python manage.py runserver
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cd src
python manage.py makemigrations accounts tutors bookings
python manage.py migrate
python manage.py seed_demo
python manage.py test
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

> If you followed the member-by-member Git workflow, each migration should normally be created in the member's own branch. Running `makemigrations` for all apps at once is only a convenient clean-install option for the completed code snapshot.

## Demo Accounts

After `python manage.py seed_demo`:

- Student: `student_demo` / `demo12345`
- Mathematics tutor: `tutor_math` / `demo12345`
- CSE tutor: `tutor_cse` / `demo12345`

These are local classroom demonstration credentials only.

## Core MVP Workflow

1. Register as a student or tutor.
2. Tutor creates or updates a tutor profile.
3. Student browses/searches tutors by subject or name.
4. Student opens a tutor profile and requests a tutoring session.
5. Tutor accepts or rejects the request from the tutor dashboard.
6. Student sees the updated request status and can cancel a pending request.

## Repository Structure

```text
online-tutoring-platform/
├── README.md
├── requirements.txt
├── docs/
│   ├── Requirement_Report.pdf
│   ├── Product_Backlog.md
│   ├── Sprint_Plan.md
│   └── Scrum_Evidence_Template.md
├── src/
│   ├── manage.py
│   ├── tutorhub/
│   ├── accounts/
│   ├── tutors/
│   ├── bookings/
│   ├── templates/
│   └── static/
├── assets/
└── screenshots/
```

## Feature Branches

- Abdullah Al Kafi: `kafi-authentication`
- Sadaf Rahman: `sadaf-tutor-discovery`
- Sakila Akter: `sakila-booking-dashboard`
