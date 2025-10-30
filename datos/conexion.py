from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# pip install sqlalchemy 
# pip install mysql-connector-python
# Definir cadena de conexión
# mysql+mysqlconnector://user:password@host:port/database_name
# Reemplazar user, password, host, port y database con tus credenciales de DB
DATABASE_URL ="mysql+mysqlconnector://catalina:Stefanny.2006@localhost:3306/boutique_db"
motor_db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=motor_db)