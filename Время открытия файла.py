import os
from datetime import datetime


def open_file_time_measure(file_type, file_path):
    """
    Print time of opening file of some type at file path

    Parameters:
        file_type (string): Type of opening file
        file_path (string): Path to file to open
    Returns:
        res_time (str): String of opening file time
    """
    start_time = datetime.now()
    os.system("start " + file_path)
    res_time = datetime.now() - start_time
    return file_type + ": " + res_time.__str__() + "\n"


with open('FileOpeningTimes.txt', 'a') as fp:
    fp.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") +
             "\n--------------------\n")
    fp.write(open_file_time_measure('HTML', "python.html"))
    fp.write(open_file_time_measure('DOCX', "fileDoc.docx"))
    fp.write(open_file_time_measure('TXT', "fileText.txt"))
    fp.write(open_file_time_measure('IMG', "imageFile.jpg"))
    fp.write(open_file_time_measure('VIDEO', "VideoFile.mp4"))
    fp.write(open_file_time_measure('AUDIO', "AUDIO.mp3"))
    fp.write("\n")

# # HTML file time measure
# start_time = datetime.now()
# os.system("start python.html")
# print("HTML: ", datetime.now() - start_time, "ms")
#
# # DOC file time measure
# start_time = datetime.now()
# os.system("start fileDoc.docx")
# print("DOCX: ", datetime.now() - start_time, "ms")
#
# # TXT file time measure
# start_time = datetime.now()
# os.system("start fileText.txt")
# print("TXT: ", datetime.now() - start_time, "ms")
#
# # IMG file time measure
# start_time = datetime.now()
# os.system("start imageFile.jpg")
# print("IMG: ", datetime.now() - start_time, "ms")
#
# # VIDEO file time measure
# start_time = datetime.now()
# os.system("start VideoFile.mp4")
# print("VIDEO: ", datetime.now() - start_time, "ms")
#
# # AUDIO file time measure
# start_time = datetime.now()
# os.system("start AUDIO.mp3")
# print("AUDIO: ", datetime.now() - start_time, "ms")
