from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# MODELOS DE DATOS!!! no analiticos
#Pydantic es mas para input y output de un endpoint no para una base de datos

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    predict_values = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, nullable=True) 