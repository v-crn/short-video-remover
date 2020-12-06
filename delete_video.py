import argparse
import os
import sys
import ffmpeg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dir',
        help='Please set a video directory',
        type=str
    )
    parser.add_argument(
        '--time',
        help='Please set a duration time[sec]',
        type=float
    )
    args = parser.parse_args()

    dir_path = args.dir if hasattr(args, 'dir') else os.getcwd()
    time = args.time if hasattr(args, 'time') else 60
    print(f'Exploring {dir_path}')
    for cd, dirs, files in os.walk(dir_path):
        for file in files:
            path = dir_path + '/' + file
            probe = ffmpeg.probe(path)
            duration = float(probe['streams'][0]['duration'])
            if duration > time:
                continue
            if os.path.exists(path):
                print(f'duration: {duration}')
                os.remove(path)
                print(f'{file} is deleted as its duration={duration}[sec] is under {time}[sec].')
            else:
                print(f"Can not delete {file} as it doesn't exists.")


if __name__ == "__main__":
    main()
