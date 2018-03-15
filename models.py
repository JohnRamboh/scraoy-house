from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

engine = create_engine('mysql+mysqldb://root@localhost:3306/house?charset=utf8')

Base = declarative_base()

class House(Base):
    __tablename__ = 'houseforms'
    
    name = Column(String(1024), primary_key = True)
    size = Column(String(512))
    describe = Column(String(1024))
    addr = Column(String(1024))
    price = Column(String(64))

if __name__ == '__main__':
	Base.metadata.create_all(engine)
