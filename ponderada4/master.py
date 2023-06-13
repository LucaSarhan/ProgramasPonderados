import os
import time
from supabase import create_client, Client

supa_url = "https://teozkfcfghiaoisnikik.supabase.co"
supa_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRlb3prZmNmZ2hpYW9pc25pa2lrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NjU4MDY1NSwiZXhwIjoyMDAyMTU2NjU1fQ.LOJAoVh6DZKRwnltuFH8pSZECFcCJboWywRvOGlwgc4"
supabase: Client = create_client(supa_url, supa_key)

# Bucket name
bucket = "Ponderado3"

# Get all archives in my media directory
list = os.listdir("./Media")

# Send every file to my bucket
for archive in list:
    with open(os.path.join("./Media", archive), 'rb+') as f:
        data = f.read()
        res = supabase.storage.from_(bucket).upload(f"{time.time()}_{archive}", data)
        print(res)
