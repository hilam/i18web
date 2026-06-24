import os

import dotenv

dotenv.load_dotenv()

dbtype, host, port, user, password, database = (
    os.getenv("DB_TYPE"),
    os.getenv("DB_HOST"),
    os.getenv("DB_PORT"),
    os.getenv("DB_USER"),
    os.getenv("DB_PASS"),
    os.getenv("DB_NAME"),
)

db_strings = {
    "postgres": f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}",
    "oracle": f"oracle+cx_oracle://{user}:{password}@{host}:{port}?service={database}",
    "mariadb": f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}",
    "mysql": f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}",
    "sqlite": f"sqlite:///./{database}"
}

if dbtype in db_strings.keys():
    db_url = db_strings.get(dbtype)
else:
    raise ValueError(f"Banco de dados não suportado! Escolha entre as opções {db_strings.keys()}")
