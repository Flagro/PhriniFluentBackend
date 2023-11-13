# 🌍 PhriniFluent Backend

![PhriniFluent Logo](logo.png)

🎉 Welcome to the *backend repository* of **PhriniFluent**, an open-source language learning platform that's all about making language learning fun and accessible! This repository is the heart and soul of PhriniFluent, powering all the amazing features our users love.

🔗 [PhriniFluent Main Project](https://github.com/Flagro/PhriniFluent)

## 📜 License
This project spreads the love with the MIT License.

## 💻 Implementation
Our backend is crafted with care using Django and Django REST Framework (DRF), with Nginx as the trusty steed serving our web content.

## 🌟 Microservices Overview

### 1. 🙋 PhriniFluentUsers
#### Model:
- `PhriniFluentUser` (inherits `AbstractUser`)
  - `telegram_handle`: CharField (max_length=100, unique, nullable, blank)

#### 🚀 API Endpoints:
- `POST /signup`: Begin your adventure by registering!
- `POST /login`: Welcome back! Time to dive in.

### 2. 📚 PhriniFluentWords
#### Models:
- `Language`: 🌐 Languages that connect our world.
- `WordGroup`: 📝 Collections of words, shared or personal.
- `WordGroupDescription`: 📖 Stories behind each word group.
- `Word`: 🧩 Individual words that paint our thoughts.
- `WordDescription`: 🖋️ Meanings and nuances of each word.

#### 🚀 API Endpoints:
- `GET /public_word_groups`: Explore public word groups.
- `GET /private_word_groups`: Your personal linguistic treasure.
- `GET /word_group/{group_id}/random_word`: Discover a random word.
- `POST /word/{word_id}/similarity`: Compare and learn.

## 🚀 Setup Instructions
1. **Docker Setup:**
   - 🏗️ Use `docker-compose up --build` to assemble and ignite the services.

2. **Database Migration:**
   - 🛠️ After the grand launch, set up the database with:
     ```
     docker-compose exec web python manage.py migrate
     ```
   - This magic spell runs the `migrate` command inside the 'web' service container.

## 👐 Collaboration
🤝 Your contributions bring PhriniFluent to life! Whether it's a bug fix, a feature, or just a bit of wisdom, we're all ears. Check out our [issues page](https://github.com/Flagro/PhriniFluentBackend/issues) for current quests and adventures!

---

💫 *Feel the joy of learning and sharing in the world of PhriniFluent!* Together, we're making language learning not just effective, but **magical**! ✨
