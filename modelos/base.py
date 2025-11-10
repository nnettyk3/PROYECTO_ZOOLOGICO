
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Float, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker

# Define la base declarativa
Base = declarative_base()