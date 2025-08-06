import hashlib
import uuid

from geoalchemy2.shape import from_shape

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    create_engine,

)
from shapely.geometry import Point
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
Base = declarative_base()
from sqlalchemy import Column, String, Integer, DateTime, func


class PrsrHotels(Base):
    __tablename__ = 'prsr_hotels'

    id = Column(CHAR(36), primary_key=True, comment='FIAS Id')  # UUID как строка
    title_hash = Column(String(32), primary_key=True, nullable=False)
    city_id = Column(CHAR(36), nullable=False, comment='FIAS id города')  # UUID как строка
    address = Column(String(512), nullable=False, comment='Адрес')
    price = Column(Integer(unsigned=True), nullable=False, comment='Цена')
    title = Column(String(255), nullable=False, comment='Название')
    hotel_title = Column(String(255), nullable=False, comment='Название отеля')
    coordinates = Column(Geometry('POINT'), nullable=False, comment='Координаты')
    created_date = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    modified_date = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)


class DatabaseHandler:
    def __init__(self, db_url='mysql+pymysql://parser:9ExtUS8uRyF9FSDf@192.168.5.27:3306/parser'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_hash(self, input_string):
        byte_string = input_string.encode('utf-8')

        # Создаем объект MD5
        md5_hash = hashlib.md5(byte_string)

        # Получаем хэш в виде шестнадцатеричной строки
        hex_digest = md5_hash.hexdigest()
        return hex_digest

    def add_PrsrHotels(self,
                  uuid,
                  city_id,
                  price,
                  title,
                  hotel_title,
                  coordinates=from_shape(Point(37.6173, 55.7558), srid=4326) ,
                  address="address",
                  ):
        maria = PrsrHotels(
            id=uuid,
            title_hash=self.get_hash(title),
            city_id=city_id,
            address=address,
            price=price,
            title=title,
            hotel_title=hotel_title,
            coordinates=coordinates,

        )
        self.session.add(maria)
        self.session.commit()

    def close(self):
        self.session.close()


# Использование
if __name__ == "__main__":
    db = DatabaseHandler('mysql+pymysql://user:password@localhost:3306/mariadb')
    db.add_PrsrHotels(
        uuid=uuid.uuid4(),
        city_id=uuid.uuid4(),
        price=1,
        title="title",
        hotel_title='hotel_title'
    )
    db.close()
