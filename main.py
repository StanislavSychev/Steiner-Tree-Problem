from heuristic_steiner_tree import heuristic_tree
from utils import visualize_tree, read_points, write_tree
from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        "input_file",
        type=str
    )
    parser.add_argument(
        "output_file",
        type=str
    )
    parser.add_argument(
        "-v", "--visualise",
        dest="visualise",
        action="store_true"
    )
    parser.set_defaults(visualise=False)
    parser.add_argument(
        "--alpha",
        type=float,
        dest="alpha",
        default=1e-2
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=100
    )
    args = parser.parse_args()
    points = read_points(args.input_file)
    size = points.shape[0]
    points, adjacentcy_list = heuristic_tree(points, alpha=args.alpha, iterations=args.iterations)
    write_tree(args.output_file, points, adjacentcy_list)
    if args.visualise:
        visualize_tree(points, adjacentcy_list, size)
