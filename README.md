HELLO FREİNDS!

this project here is simple yet effective. welcome to the Password Manager App

# 🔐 Password Manager (Because My Brain Is Not a Database)

## Why This Exists (A Slightly Embarrassing Story)

At some point in my life, I lost my phone.

Along with it, I lost **every saved password**, every auto-login, every "don’t worry, future me will remember this" credential.

Future me did **not** remember.

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

It does not try to be fancy.
It does not upload your data anywhere.
It just **stores and retrieves credentials** so you don’t have to rely on your brain under stress.

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

No scrolling through files.
No guessing which password goes where.

---

### 🔑 Password Generator

Some websites insist on passwords that look like encrypted alien language.

This app includes a **password generator** so you don’t have to:

* Invent one yourself
* Reuse weak passwords
* Stare at the keyboard in frustration

Is it going to fix the entire industry’s password policy problem?

Well… no.

But I did my part.

---

## Data Storage

* All data is stored **locally**
* Format: **JSON**
* No cloud
* No tracking
* No network calls

You own your data.

---

## Who This Is For

* People who forget passwords
* People who hate password rules
* People who lost a phone once and learned the hard way
* People who like simple tools that just work

---

## Who This Is *Not* For

* Enterprise-level security use
* Cloud-based password syncing
* Anyone expecting military-grade encryption (yet)

This is a **personal utility**, not a replacement for professional password vaults.

---

## Tech Stack

* Python
* Tkinter (GUI)
* JSON (storage)

Simple, readable, and easy to extend.

---

## Final Words

There’s an open-source contributor out there named Jeff Atwood, the co‑founder of Stack Overflow who once said:

  “password rules are bullshit” and pointed out that a lot of these arbitrary requirements don’t actually make things more secure.

I didn’t fix the whole problem.

But I fixed **my** problem and might be yours aswell.

i didn't made these companies stop making these arbitrary requirements but i will make it so that you login without being frustrated by them
The rules may still exist, but at least now you can generate, store, and retrieve passwords without losing your sanity.



And now I don’t panic when I see a login screen.

---

If you want to improve it, break it, extend it, or just laugh at the origin story welcome aboard and i hope to see you in my journey of being confused.

