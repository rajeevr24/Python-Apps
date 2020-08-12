from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
rows = session.query(Table).all()
while True:
    print('''1) Today's tasks
2) Add task
0) Exit''')
    menu = input()
    if menu == '0':
        print('\nBye!')
        break
    elif menu == '1':
        if len(rows) == 0:
            print('\nToday:\nNothing to do!\n')
        else:
            for i in range(len(rows)):
                print('\nToday:\n' +
                      str(rows[i].id) + '.', rows[i].task + '\n')
    elif menu == '2':
        new_row = Table(task=input('\nEnter task\n'))
        session.add(new_row)
        session.commit()
