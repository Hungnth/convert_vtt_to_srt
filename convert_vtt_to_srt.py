import os
import webvtt


def vtt_to_srt(vtt_path, srt_path):
    # Parse the VTT file into a list of cue objects
    with open(vtt_path, 'r') as vtt_file:
        cues = list(webvtt.read(vtt_path))

        # Open the SRT file for writing with the utf-8 encoding
        with open(srt_path, 'w', encoding='utf-8') as srt_file:
            # Iterate over the cues
            for i, cue in enumerate(cues):
                # Write the cue number
                srt_file.write(str(i + 1) + '\n')

                # Write the start and end times
                srt_file.write(cue.start + ' --> ' + cue.end + '\n')

                # Write the text of the cue
                srt_file.write(cue.text + '\n\n')


def convert_vtt_to_srt(root_dir):
    # Iterate over all files in the directory and its subdirectories
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # If the file is a VTT file
            if file.endswith('.vtt'):
                # Construct the full path of the VTT file
                vtt_path = os.path.join(root, file)

                # Construct the full path of the SRT file
                srt_path = os.path.splitext(vtt_path)[0] + '.srt'

                # Convert the VTT file to an SRT file
                vtt_to_srt(vtt_path, srt_path)


# Call the function to convert all VTT files in the current directory and its subdirectories
convert_vtt_to_srt('.')
