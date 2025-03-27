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
        "-o", "--output", type=str, default = None,  help="Output video file name (optional)"
    )
    return parser


def determine_output_path(input_file, output_file):
    input_dir, input_filename = os.path.split(input_file)
    name, _ = os.path.splitext(input_filename)
    
    if output_file:
        output_dir, output_filename = os.path.split(output_file)
        if not output_dir:  # If no directory is specified, use input file's directory
            return os.path.join(input_dir, output_filename)
        return output_file
    else:
        return os.path.join(input_dir, f"{name}_volume.mp4")

class ViztoolzPlugin:
    """Increase decrease volume"""

    __name__ = "volume"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        output = determine_output_path(args.input_video,args.output )

        adjust_volume(args.input_video, args.volume_db, output)

    def hello(self, args):
        # this routine will be called when "vidtoolz "volume is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


volume_plugin = ViztoolzPlugin()
