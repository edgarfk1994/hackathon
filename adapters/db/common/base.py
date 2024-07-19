from sqlmodel import Session, create_engine, SQLModel

engine = create_engine("postgresql://Finkargo:Finkargo@localhost:5432/Finkargo")
SQLModel.metadata.create_all(engine)
session = Session(engine)

def get_db():
    with Session(engine) as session:
        yield session
