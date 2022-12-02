# super janky but ok for now

import pickle
from os.path import exists

CACHEFILE = "tweetcache.p"

if not exists(CACHEFILE):
    with open(CACHEFILE, "wb") as df:
        pickle.dump({}, df)

def update_cache(uid, data):
    with open(CACHEFILE, 'rb') as df:
        db = pickle.load(df)
    if uid not in db:
        db[uid] = []
    for d in data:
        if d not in db[uid]:
            db[uid].append(d)
    with open(CACHEFILE, 'wb') as df:
        pickle.dump(db, df)

def get_cache(uid):
    with open(CACHEFILE, 'rb') as df:
        db = pickle.load(df)
    return db.get(uid, [])

    
def is_cached(uid, data):
    print("checking cache")
    with open(CACHEFILE, 'rb') as df:
        db = pickle.load(df)
        cachedata = db.get(uid, [])
    for d in data:
        if d not in cachedata:
            return False
    return True