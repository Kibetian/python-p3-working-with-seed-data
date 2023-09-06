#!/usr/bin/env python3

from faker import Faker  # Add this import
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    botw = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
    ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
    mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)
    ccs = Game(title="Candy Crush Saga", platform="Mobile", genre="Puzzle", price=0)

    session.bulk_save_objects([botw, ffvii, mk8])
    session.commit()

    session.query(Game).count()
    # => 3
    session.query(Game)[1]
    # => Game(id=3, title="Mario Kart 8", platform="Switch)"


    print("Seeding games...")

games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
for i in range(50)]

session.bulk_save_objects(games)
session.commit()


print(session.query(Game).count())
# => 50
session.query(Game).first()
# => Game(id=1, title="Lisa Barton", platform="hotel)"
session.query(Game)[1]
# => Game(id=50, title="Jesus Anderson", platform="meeting)"
