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
            '/': {
                'dirs': [],
                'files': {}
            }
        }
        curr_dir = ''

        # create initial stacks
        while True:
            line = f.readline()
            cmd = line.rstrip()
            if cmd == '':
                break

            if is_mv_root(cmd):
                previous_dir = curr_dir
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
                previous_dir = curr_dir
                curr_dir = full_dir_name
                continue

        # pprint(directories)

        total = 0
        for dir_name in directories.keys():
            dir_size = calculate_dir_size(dir_name)
            # print(f'dir {dir_name}, size: {dir_size}')
            if dir_size <= 100000:
                # print(f' >> dir {dir_name}, size: {dir_size} < threshold')
                total += dir_size

        # part 1
        print(f'total: {total}')

        # part 2
        required_space = 30000000
        used_space = calculate_dir_size('')
        unused_space = 70000000 - used_space
        min_size = 70000000
        minimum_space_to_delete = required_space - unused_space

        for dir_name in directories.keys():
            dir_size = calculate_dir_size(dir_name)
            if dir_size >= minimum_space_to_delete:
                if dir_size < min_size:
                    min_size = dir_size
                    print(f'found minimum size dir {dir_name} with {dir_size}')
