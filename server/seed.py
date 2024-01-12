#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app
from models import db, Owner, Pet

# Populate db
def seed_data():
    owner1 = Owner(name="marcus",pets="flax")
    owner2 = Owner(name="gustavo",pets="whiskers")

    db.session.add(owner1)
    db.session.add(owner2)
    db.session.commit() 


    pet1=Pet(name="flax", species="lebron", owner_id=owner2.id)
    pet2=Pet(name="whiskers", species="sango", owner_id=owner1.id)

    #commit
    db.session.add(pet1)
    db.session.add(pet2)
    db.session.commit()



if __name__ =='__main__':
    with app.app_context():
        print("Seeding started -----")
        #seed_data()
        print("Seeded successfully")


    