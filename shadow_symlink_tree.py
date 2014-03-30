import os
import argparse
from os.path import join, getsize


def symlink_files(source_dir,
                  dest_dir,
                  remove_string,
                  replacement_string,
                  verbose):

    for root, dirs, files in os.walk(source_dir):
        # create the shadow directory structure
        for d in dirs:
            source_path = os.path.join(root, d)
            dest_path = source_path.replace(source_dir, dest_dir, 1)
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
        # now create the sym links to the files and replace the chars
        for f in files:
            source_path = os.path.join(root, f)
            dest_path = source_path.replace(source_dir, dest_dir, 1)
            (path, filename) = os.path.split(dest_path)
            (filename, ext) = os.path.splitext(filename)
            clean_filename = filename.replace(remove_string,
                                              replacement_string)
            symlink_name = os.path.join(path, clean_filename + ext)
            if verbose:
                if not filename == clean_filename:
                    print 'replaced ' + filename + ' with ' + clean_filename + ext

            if not os.path.lexists(symlink_name):
                os.symlink(source_path, symlink_name)
                if verbose:
                    print 'linking ' + source_path + ' ' + symlink_name
            else:
                if verbose:
                    print 'skipping ' + source_path + ' ' + symlink_name


def main():
    parser = argparse.ArgumentParser(description='Create shadow symlink tree'
                                     ' and replacing characters in the '
                                     'filenames.'
                                     'eg. foo.bar.txt -> foo_bar.txt')
    parser.add_argument('--replace', help='replace the characters in the'
                                          ' filename', action='store_true')
    parser.add_argument('--rmstr', help='string to remove')
    parser.add_argument('--rpstr', help='string to replace')
    parser.add_argument('--verbose', help='verbose on', action='store_true')
    parser.add_argument('src_dir', help='source directory')
    parser.add_argument('dst_dir', help='destination directory')
    parser.add_argument('--force', help='force creation of destination'
                                        ' directory', action='store_true')
    args = parser.parse_args()

    source_dir = args.src_dir
    dest_dir = args.dst_dir
    remove_string = args.rmstr
    replacement_string = args.rpstr
    force_dir_creation = args.force
    verbose = args.verbose

    if not os.path.exists(source_dir) or not os.path.exists(dest_dir):
        if not os.path.exists(dest_dir):
            if force_dir_creation:
                os.makedirs(dest_dir)
            else:
                print 'destination directory does not exist', dest_dir
                exit(1)
        if not os.path.exists(source_dir):
            print 'source directory does not exist', source_dir
            exit(1)

    if args.replace:
        if not remove_string or not replacement_string:
            if not remove_string:
                print 'define string to remove'
            if not replacement_string:
                print 'define replacement string'
            exit(1)
    else:
        replacement_string = ''
        remove_string = ''

    symlink_files(source_dir,
                  dest_dir,
                  remove_string,
                  replacement_string,
                  verbose)

if __name__ == "__main__":
    main()
