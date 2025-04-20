#Write a function called replace_all that takes as arguments a pattern string, a replacement string, and two filenames. It should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the contents, it should be replaced with the replacement string
def replace_all(pat_string, rep_string, source_path, dest_path):
    with open(source_path, 'r') as reader:
        contents = reader.read()
    updated_contents = contents.replace(pat_string, rep_string)
    with open(dest_path, 'w') as writer:
        writer.write(updated_contents)

replace_all('photos', 'images', 'photos/notes.txt', 'photos/new_notes.txt')
