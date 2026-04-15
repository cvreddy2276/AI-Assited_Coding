# reStructuredText (reST) style
def read_file_rest(filename):
	"""
	Reads the contents of a file.

	:param filename: The path to the file to read.
	:type filename: str
	:return: The contents of the file.
	:rtype: str
	:raises FileNotFoundError: If the file does not exist.
	:raises IOError: If an I/O error occurs.
	"""
	with open(filename, 'r') as f:
		return f.read()

# Google style
def read_file_google(filename):
	"""
	Reads the contents of a file.

	Args:
		filename (str): The path to the file to read.

	Returns:
		str: The contents of the file.

	Raises:
		FileNotFoundError: If the file does not exist.
		IOError: If an I/O error occurs.
	"""
	with open(filename, 'r') as f:
		return f.read()

# NumPy style
def read_file_numpy(filename):
	"""
	Reads the contents of a file.

	Parameters
	----------
	filename : str
		The path to the file to read.

	Returns
	-------
	str
		The contents of the file.

	Raises
	------
	FileNotFoundError
		If the file does not exist.
	IOError
		If an I/O error occurs.
	"""
	with open(filename, 'r') as f:
		return f.read()
