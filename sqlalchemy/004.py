
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, CheckConstraint
from sqlalchemy.sql import func
from datetime import datetime 
from sqlalchemy import select

metadata = MetaData()

engine = create_engine("mysql+mysqldb://root:root@localhost/hello")

conn = engine.connect() 
 
c = [
    
    ##  date/time functions  ##
    
    #func.timeofday(), # for postgresql
    func.localtime(),
    func.current_timestamp(),    
    #func.date_part("month", func.now()),        # for postgresql
    func.now(),
    
    ##  mathematical functions  ##
    
    func.pow(4,2),
    func.sqrt(441),
    func.pi(),        
    func.floor(func.pi()),
    func.ceil(func.pi()),
    
    ##  string functions  ##
    
    func.lower("ABC"),
    func.upper("abc"),
    func.length("abc"),
    func.trim("  ab c  "),    
    #func.chr(65),        # for postgresql
]
 
s = select(c)
rs = conn.execute(s)
print(rs.keys())
print(rs.fetchall())
