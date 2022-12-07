from pprint import pprint


def is_mv_root(cmd):
    return cmd == "$ cd /"


def is_mv_back(cmd):
    return cmd == "$ cd .."


def is_list(cmd):
    return cmd == "$ ls"


def is_dir(cmd):
    return cmd.startswith('dir')


def is_file(cmd):
    return cmd[0].isnumeric()


def is_mv_dir(cmd):
    return cmd.startswith('$ cd ') and not is_mv_back(cmd)


def calculate_dir_size(dir_name):
    files_in_dir = directories[dir_name]['files']
    size_files = sum(list(files_in_dir.values()))
    subdirectories = directories[dir_name]['dirs']
    size_subdirs = sum([calculate_dir_size(subdir) for subdir in subdirectories])
    return size_files + size_subdirs


if __name__ == "__main__":

    with open('../../days_inputs/day-07.txt', 'r') as f:

        directories = {
            '': {
                'dirs': [],
                'files': {}
            }
        }
        curr_dir = ''

        while True:
            line = f.readline()
            cmd = line.rstrip()
            if cmd == '':
                break

            if is_mv_root(cmd):
                curr_dir = ''
                continue

            if is_mv_back(cmd):
                curr_dir = '/'.join(curr_dir.split('/')[:-1])
                continue

            if is_list(cmd):
                if curr_dir not in directories:
                    directories[curr_dir] = {
                        'dirs': [],
                        'files': {}
                    }

            if is_dir(cmd):
                dir_name = cmd.replace('dir ', '')
                full_dir_name = f'{curr_dir}/{dir_name}'
                directories[curr_dir]['dirs'].append(full_dir_name)
                continue

            if is_file(cmd):
                size, file = tuple(cmd.split())
                size = int(size)
                directories[curr_dir]['files'][file] = size
                continue

            if is_mv_dir(cmd):
                dir_name = cmd.split()[2]
                full_dir_name = f'{curr_dir}/{dir_name}'
                curr_dir = full_dir_name
                continue

        # pprint(directories)

        # part 2
        required_space = 30000000
        # get the used space in the outermost directory
        used_space = calculate_dir_size('')
        total_space = 70000000
        # calculated unused space and then the minimum space that has to be deleted
        # for being able to make the update
        unused_space = total_space - used_space
        minimum_space_to_delete = required_space - unused_space

        # initialize the minimum dir size found (for part 2 search) with a large number
        min_size = total_space

        # initialize the total size (for part 1)
        total = 0

        for dir_name in directories.keys():
            dir_size = calculate_dir_size(dir_name)
            # print(f'dir {dir_name}, size: {dir_size}')

            # check if dir size is at most the threshold (part 1)
            if dir_size <= 100000:
                total += dir_size

            # check if dir size is the smallest dir with the required size (part 2)
            if minimum_space_to_delete <= dir_size < min_size:
                min_size = dir_size
                print(f'[part2] found minimum size dir {dir_name} with {dir_size}')

        # part 1 - 2031851
        print(f'[part1] total: {total}')
        # part 2 - 2568781
