from PIL import Image, ImageOps
import argparse
import os

def main(file_path, desired_size=[2350, 1950]):
    im = Image.open(file_path)
    old_size = im.size  # old_size[0] is in (width, height) format
    ratio = float(max(desired_size))/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    # im.thumbnail(new_size, Image.ANTIALIAS)
    im = im.resize(new_size, Image.ANTIALIAS)
    # create a new image and paste the resized on it
    new_im = Image.new("RGB", (desired_size[0], desired_size[1]))
    new_im.paste(im, ((desired_size[0]-new_size[0])//2,
                        (desired_size[1]-new_size[1])//2))

    delta_w = desired_size[0] - new_size[0]
    delta_h = desired_size[1] - new_size[1]
    padding = (delta_w//2, delta_h//2, delta_w-(delta_w//2), delta_h-(delta_h//2))
    new_im = ImageOps.expand(im, padding, fill="white")

    filename, file_extension = os.path.splitext(file_path)
    new_im.save(filename + "_cover" + file_extension)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-fpath', '--FILE_PATH', action="store",
                        default="", type=str,
                        help='Path to image that you want to resize to thumbnail format.')
    args = parser.parse_args()
    main(args.FILE_PATH)
