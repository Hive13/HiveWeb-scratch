# The New HiveWeb

This will be the main README for the new Hive intweb. I'm starting a
todo list/task list here.

This README will also serve (for now) as the main page for documentation. 

---

### Thoughts and Ideas

###### Let's also have a place for thoughts and ideas, eh? 

* we should define what a bug report looks like
* we should define what a decent contribution looks like
* should we assign 1 or 2 people to review PRs before merging? Recurring meeting time instead?
* What HTTP framework/server for the backend? Flask? (And what about for HTTPS/SSL for both device access and frontend access?)
* What do we want on the frontend? Django?
* We might focus some bootstrapping along these lines (even if the design still
  has to change):
  - Enough of functioning DB layer & API in order to handle access
    queries for devices (like to query door access from a badge).
  - Initially have a Raspberry Pi (perhaps with something light and
    bulletproof like Alpine Linux) interacting with HiveWeb, the RFID
    reader, and the lock electronics in order to replace the current
    electronics if needed.  Document this copiously.
  - Develop the same functionality for ESP32 and maybe ESP8266 so that
    the board from Sparks can be used.  Aim for a reusable library.

---

### Tasks

- [ ] API route tree - will give us an idea of what routes we need and the functionality they'll provide
- [ ] Bootstrap new API (includes folder structure, framework adoption)
- [ ] Backend unit testing
- [ ] Model layer in Python & SQLAlchemy
  - [ ] Convert schema to SQLAlchemy (partially done)
  - [ ] Start implementing actual queries of interest
  - [ ] Convert relevant business logic (API may need to be further along for this)

---

### Documentation

* something will go here soon, I promise. 
* Some docs belong on the Wiki too. Let's try to: update or remove
  outdated Wiki packages, put links on relevant Wiki pages to things
  that are documented in the GitHub, and vice versa.
* See also:
  - https://wiki.hive13.org/view/RFID_Access
  - https://wiki.hive13.org/view/RFID_Card (needs updates)