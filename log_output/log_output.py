import time
import uuid
from datetime import datetime, timezone
random_string = str(uuid.uuid4())

while True:
    timestamp = datetime.now(timezone.utc).isoformat() + "Z"
    timestamp = timestamp.replace("+00:00Z", "Z")
    print(f"{timestamp}: {random_string}")
    time.sleep(5)
