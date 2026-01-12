
# PyMotivator

## Project Overview

PyMotivator is a Python-based daily WhatsApp quote sender that delivers motivational, happiness, success, and other themed quotes based on the day of the week.  
It uses local offline quote libraries (`quoteslib` and `inspirational-quotes`) to avoid API dependencies. The project schedules daily messages using APScheduler and sends quotes via Twilio WhatsApp API.

---

## Features

- Sends themed quotes daily on WhatsApp based on day of the week
- Uses offline Python libraries for quotes (no internet/API dependency)
- Schedules message sending with APScheduler (cron-based)
- Modular and clean folder structure
- Easily deployable as a background worker (e.g., on Render)

---

## To Do

- [ ] Implement non-repeating quote logic (currently repeats possible)
- [ ] Expand local quote database or integrate custom JSON dataset
- [ ] Add support for multiple phone numbers / recipients
- [ ] Add logging and error handling for Twilio message failures
- [ ] Create Docker container for easy deployment
- [ ] Add UI/dashboard to manage quotes and scheduling
- [ ] Implement persistence for sent quotes (DB or file)
- [ ] Add unit tests and CI/CD pipeline

---

## Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set environment variables

| Variable            | Description              |
|---------------------|--------------------------|
| TWILIO_ACCOUNT_SID  | Your Twilio Account SID   |
| TWILIO_AUTH_TOKEN   | Your Twilio Auth Token    |
| PHONE               | WhatsApp phone number (e.g. whatsapp:+919999999999) |

Example (Linux/macOS):

```bash
export TWILIO_ACCOUNT_SID=your_account_sid
export TWILIO_AUTH_TOKEN=your_auth_token
export PHONE=whatsapp:+919999999999
```

### 3. Run scheduler

```bash
python cron.py
```

---

## Deploy on Render

- Create a new **Background Worker** service
- Connect your GitHub repo containing this project
- Set build command: `pip install -r requirements.txt`
- Set start command: `python cron.py`
- Add environment variables in Render Dashboard
- Deploy and your daily WhatsApp quotes will start sending automatically!

---

## License

MIT License © 2026

---

*Created by [Your Name]*
