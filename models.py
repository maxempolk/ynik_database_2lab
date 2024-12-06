from datetime import datetime
import uuid
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, nullable=False)
    is_banned = Column(Boolean, default=False)
    game_mode = Column(String)
    health = Column(Float, default=20.0)
    hunger = Column(Float, default=20.0)
    experience = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    location = relationship("PlayerLocation", back_populates="player", uselist=False)
    inventory = relationship("Inventory", back_populates="player")
    statistics = relationship("PlayerStatistics", back_populates="player")
    achievements = relationship("PlayerAchievement", back_populates="player")
    permissions = relationship("Permission", back_populates="player")
    economy = relationship("Economy", back_populates="player")
    warps = relationship("Warp", back_populates="player")
    chat_logs = relationship("ChatLog", back_populates="player")

class World(Base):
    __tablename__ = 'worlds'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    seed = Column(String)
    difficulty = Column(String)
    spawn_x = Column(Float)
    spawn_y = Column(Float)
    spawn_z = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class PlayerLocation(Base):
    __tablename__ = 'player_locations'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    player_id = Column(UUID(as_uuid=True), ForeignKey('players.id'))
    world_id = Column(UUID(as_uuid=True), ForeignKey('worlds.id'))
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    yaw = Column(Float)
    pitch = Column(Float)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    player = relationship("Player", back_populates="location")
    world = relationship("World")

class Inventory(Base):
    __tablename__ = 'inventories'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    player_id = Column(UUID(as_uuid=True), ForeignKey('players.id'))
    slot = Column(Integer)
    item_id = Column(String)
    quantity = Column(Integer)
    durability = Column(Float)
    
    player = relationship("Player", back_populates="inventory")

class Economy(Base):
    __tablename__ = 'economy'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    player_id = Column(UUID(as_uuid=True), ForeignKey('players.id'))
    balance = Column(Float, default=0)
    last_transaction = Column(DateTime)
    
    player = relationship("Player", back_populates="economy")

class PlayerStatistics(Base):
    __tablename__ = 'player_statistics'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    player_id = Column(UUID(as_uuid=True), ForeignKey('players.id'))
    blocks_broken = Column(Integer, default=0)
    blocks_placed = Column(Integer, default=0)
    kills = Column(Integer, default=0)
    deaths = Column(Integer, default=0)
    play_time = Column(Integer, default=0)  # in minutes
    
    player = relationship("Player", back_populates="statistics")

class Achievement(Base):
    __tablename__ = 'achievements'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True)
    description = Column(String)
    points = Column(Integer)

class PlayerAchievement(Base):
    __tablename__ = 'player_achievements'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    player_id = Column(UUID(as_uuid=True), ForeignKey('players.id'))
    achievement_id = Column(UUID(as_uuid=True), ForeignKey('achievements.id'))
    date_earned = Column(DateTime, default=datetime.utcnow)
    
    player = relationship("Player", back_populates="achievements")
    achievement = relationship("Achievement")

class Permission(Base):
    __tablename__ = 'permissions'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    player_id = Column(UUID(as_uuid=True), ForeignKey('players.id'))
    role = Column(String)
    permission_node = Column(String)
    granted = Column(Boolean, default=True)
    
    player = relationship("Player", back_populates="permissions")

class Warp(Base):
    __tablename__ = 'warps'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    player_id = Column(UUID(as_uuid=True), ForeignKey('players.id'))
    name = Column(String)
    world_id = Column(UUID(as_uuid=True), ForeignKey('worlds.id'))
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    is_home = Column(Boolean, default=False)
    
    player = relationship("Player", back_populates="warps")
    world = relationship("World")

class ChatLog(Base):
    __tablename__ = 'chat_logs'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    player_id = Column(UUID(as_uuid=True), ForeignKey('players.id'))
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    is_command = Column(Boolean, default=False)
    
    player = relationship("Player", back_populates="chat_logs")