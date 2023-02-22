from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from django.conf import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()


class CdcConn(Base):
    __tablename__ = 'cdc_conn'
    id = Column(Integer, primary_key=True)
    conn_type = Column(String(128))
    conn_name = Column(String(128), nullable=False)

    __table_args__ = (
        UniqueConstraint('conn_name', 'id', name='_conn_name_id_uc'),
    )


class CdcFields(Base):
    __tablename__ = 'cdc_fields'
    id = Column(Integer, primary_key=True)
    table_id = Column(String(128), nullable=False)
    source_field_name = Column(String(128), nullable=False)
    target_field_name = Column(String(128))
    field_index = Column(Numeric(6, 0))
    field_type = Column(String(40))
    modified_time = Column(DateTime)
    pk_field = Column(Numeric(10, 0))
    required = Column(Numeric(10, 0))

    __table_args__ = (
        UniqueConstraint('table_id', 'source_field_name', 'id',
                         name='_table_id_source_field_name_id_uc'),
    )


class CdcStatus(Base):
    __tablename__ = 'cdc_status'
    id = Column(Integer, primary_key=True)
    table_id = Column(String(128), nullable=False)
    last_read_seq = Column(String(35))
    init_read_seq = Column(String(35))

    __table_args__ = (
        UniqueConstraint('table_id', 'id', name='_table_id_id_uc'),
    )


class CdcTables(Base):
    __tablename__ = 'cdc_tables'
    id = Column(Integer, primary_key=True)
    table_id = Column(String(128), nullable=False)
    source_db = Column(String(128))
    source_schema = Column(String(128))
    source_table = Column(String(128))
    target_schema = Column(String(128))
    target_table = Column(String(128))
    uppercase_fields = Column(Numeric(18, 0))
    filter = Column(String(128))
    force_init = Column(String(128))
    cntrl_fld = Column(String(128))

    cdc_fields = relationship('CdcFields', backref='cdc_table')

    __table_args__ = (
        UniqueConstraint('table_id', 'id', name='_table_id_id_uc'),
    )


Session = sessionmaker(bind=engine)
