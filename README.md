HELLO FREİNDS!

this project here is simple yet effective. welcome to the Password Manager App

# 🔐 Password Manager

## Why This Exists (A Slightly Embarrassing Story)

At some point in my life, I lost my phone.

Along with it, I lost **every saved password**, every auto-login, every "don’t worry, future me will remember this" credential.

oh buy, future me failed, Future me did **not** remember.

I ended up resetting accounts, recreating passwords, verifying emails I forgot I even owned, and staring at login screens asking for:

> *At least 12 characters, one symbol, one uppercase letter, one lowercase letter, one number, no spaces, no joy.*

That was the moment I realized:

* My memory is unreliable
* Password rules are getting absurd
* I should probably build something instead of complaining

So… this app was born.

---

## What This App Does

This is a **simple, local password / credential manager**.

It does not upload your data anywhere.
It just **stores and retrieves credentials** so you don’t have to rely on your brain under stress and it does all in local json file.

---

## Core Features

### ✅ Save Credentials

The app takes **three inputs**:

* **Website** (required)
* **Password** (required)
* **Email / Username** (optional)

When you press **Save**:

* Your credentials are stored locally
* They are saved in a **JSON file**
* Each website acts as a key tied to its credentials

---

### 🔍 Search Credentials

* Enter a website name
* Press **Search**
* The app fetches the saved credentials for that website


---

### 🔑 Password Generator

Some websites insist on passwords that look like encrypted alien language.

This app includes a **password generator** so you don’t have to:

* Invent one yourself
* Reuse weak passwords
* Stare at the keyboard in frustration
* copied in the clipboard and ready for paste right after generating (it does this using [pyperclip](https://pypi.org/project/pyperclip/))

## Data Storage

* All data is stored **locally**
* Format: **JSON**
* No cloud
* No tracking
* No network calls

You own your data.



---

## Tech Stack

* Python
* Tkinter (GUI)
* JSON (storage)
* pyperclip

## Setup
To use the clipboard features, install the dependency:

```bash
pip install pyperclip
```
---

> [!NOTE]
> If you want to improve it, break it, extend it, or just laugh at the origin story, welcome aboard! I hope to see you in my journey.

