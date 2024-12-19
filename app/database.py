
DATABASE_URL = "mysql+asyncmy://root:kwarteng@localhost:3401/Hyperfit"

engine = create_async_engine(DATABASE_URL,echo = True)