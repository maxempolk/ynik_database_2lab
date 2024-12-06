# Minecraft Server Database

A comprehensive SQLAlchemy-based database system for managing a Minecraft-like game server.

## Features

- **Player Management**
  - Basic player information (UUID, username, game mode)
  - Player metrics (health, hunger, experience)
  - Ban status tracking

- **World System**
  - World parameters management
  - Spawn point coordinates
  - Difficulty settings

- **Location Tracking**
  - Real-time player coordinates
  - View direction (yaw, pitch)
  - World position management

- **Inventory System**
  - Item management
  - Durability tracking
  - Slot-based organization

- **Economy**
  - Player balances
  - Transaction history
  - Economic metrics

- **Statistics**
  - Blocks broken/placed
  - Player kills/deaths
  - Playtime tracking

- **Achievements**
  - Progress tracking
  - Reward system
  - Completion timestamps

- **Permissions**
  - Role-based access control
  - Permission nodes
  - User groups

- **Warps & Homes**
  - Teleportation points
  - Home locations
  - Coordinate storage

- **Chat System**
  - Message history
  - Command logging
  - Moderation tools

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/minecraft-server-db.git
cd minecraft-server-db
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure database:
- Open `database.py`
- Update the PostgreSQL connection URL with your credentials:
```python
DATABASE_URL = "postgresql://username:password@localhost:5432/minecraft_db"
```

4. Initialize the database:
```bash
python -c "from database import init_db; init_db()"
```

5. Run database migrations:
```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Project Structure

- `models.py` - SQLAlchemy models and relationships
- `database.py` - Database configuration and connection
- `alembic.ini` - Migration configuration
- `requirements.txt` - Project dependencies

## Technologies

- Python 3.8+
- SQLAlchemy 2.0+
- PostgreSQL
- Alembic

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

# 2. Install dependencies:
pip install -r requirements.txt

# 3. Configure database:
- Open database.py
- Update the PostgreSQL connection URL with your credentials:

DATABASE_URL = "postgresql://username:password@localhost:5432/minecraft_db"

# 4. Initialize the database:

alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

Project Structure
models.py - SQLAlchemy models and relationships
database.py - Database configuration and connection
alembic.ini - Migration configuration
requirements.txt - Project dependencies
Technologies
Python 3.8+
SQLAlchemy 2.0+
PostgreSQL
Alembic
License
MIT License

Contributing
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request


