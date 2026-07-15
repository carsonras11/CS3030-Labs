import shutil
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

shutil.make_archive(
	f"section1_backup_{today}",
	"zip",
	"../../section1"
)
