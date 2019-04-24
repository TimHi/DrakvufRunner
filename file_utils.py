def open_file(path_to_file):
    try:
        file_handle = open(path_to_file)
    except IOError:
        logging.error("Could not read file: %s", path_to_file)
        sys.exit()
    finally:
        return file_handle