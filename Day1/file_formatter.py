def file_formatter(file_path: str) -> list:
	with open(file_path, "r") as cal:
		return cal.read().split("\n\n")
