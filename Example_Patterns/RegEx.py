
version_pattern = re.compile('Version ([0-9]*\.[0-9]*\.[0-9])')
version = re.search(version_pattern, version_output)
version = version_pattern.search(version_output)
version_string = version.group(1) # get the version part
version_numbers = version_string.split('.')
