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

#### 🚀 Words API Endpoints:
- `GET /phrini_fluent_words/word-groups/public/`: Explore public word groups.
- `GET /phrini_fluent_words/word-groups/private/`: Your personal linguistic treasure.
- `GET /phrini_fluent_words/word-groups/{group_id}/random`: Discover a random word.
- `POST /phrini_fluent_words/words/{word_id}/similarity`: Compare and learn.

## 🚀 Setup Instructions
1. **Docker Setup:**
   - 🏗️ Use `docker-compose up --build` to assemble and ignite the services.

2. **Database Migration:**
   - 🛠️ After the grand launch, set up the database with:
     ```
     docker-compose exec web python manage.py migrate
     ```
   - This magic spell runs the `migrate` command inside the 'web' service container.

### 🚀 Local setup

#### 🚀 Run migration inside container:
```bash
docker exec -it phrinifluentbackend-web-1 python manage.py migrate
```

#### 🚀 Import words using admin console:
1. Create a user in your docker image: `docker exec -it phrinifluentbackend-web-1 python manage.py createadmin`
2. Go to the admin panel in your browser: `http://127.0.0.1:8000/admin/login/?next=/admin/` and enter credentials from your env file.
3. Trigger the endpoint in your browser: `http://127.0.0.1:8000/phrini_fluent_users/import-words/` that will import the default words list.

## 👐 Collaboration
🤝 Your contributions bring PhriniFluent to life! Whether it's a bug fix, a feature, or just a bit of wisdom, we're all ears. Check out our [issues page](https://github.com/Flagro/PhriniFluentBackend/issues) for current quests and adventures!

---

💫 *Feel the joy of learning and sharing in the world of PhriniFluent!* Together, we're making language learning not just effective, but **magical**! ✨
