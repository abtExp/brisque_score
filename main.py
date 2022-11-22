import cv2
from qual import QUALITY_CHECKER
from argparse  import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    
    parser.add_argument('-p', '--path', help='Path to the image', required=True)
    
    args = parser.parse_args()
    
    checker = QUALITY_CHECKER('./model')
    
    img = cv2.imread(args.path)
    
    checker.is_good_quality(img)