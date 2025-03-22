import vidtoolz
import subprocess
import os


def adjust_volume(input_video, volume_db, output_video):
    command = [
        "ffmpeg",
        "-i",
        input_video,
        "-filter:a",
        f"volume={volume_db}dB",
        output_video,
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Volume adjusted and saved to {output_video}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def create_parser(subparser):
    parser = subparser.add_parser("volume", description="Increase decrease volume")
    # Add subprser arguments here.
    parser.add_argument("input_video", type=str, help="Path to the input video file")
    parser.add_argument(
        "volume_db",
        type=float,
        help="Volume adjustment in dB (e.g., 3 for +3dB, -3 for -3dB)",
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Output video file name (optional)"
    )
    return parser


class ViztoolzPlugin:
    """Increase decrease volume"""

    __name__ = "volume"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        # Get the directory of the input video
        input_dir = os.path.dirname(args.input_video)
        # If output is not provided, use the input video name with a modified extension
        if args.output:
            output_video = args.output
        else:
            output_video = os.path.join(
                input_dir, f"output_{os.path.basename(args.input_video)}"
            )

        adjust_volume(args.input_video, args.volume_db, output_video)

    def hello(self, args):
        # this routine will be called when "vidtoolz "volume is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


volume_plugin = ViztoolzPlugin()
