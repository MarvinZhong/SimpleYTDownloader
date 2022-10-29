import os
import PySimpleGUI as sg
from pytube import YouTube

def main():

    sg.theme('DarkTeal9')   # Add a touch of color

    # All the stuff inside your window.
    layout = [  
                [sg.Text('Enter the URL of the YouTube video you want to download', tooltip='Youtube Downloader Just Works')],
                [sg.InputText(key='-URL-')],
                [sg.Button('Video', expand_x=True, key='-VIDEO-'), sg.Button('Audio', expand_x=True, key='-AUDIO-')],
                [sg.Text(key='-OUTPUT-')]
            ]

    # Create the Window
    window = sg.Window('Simple YouTube Downloader', layout,font='Serif 12', element_justification='center', resizable=True)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        # donwload Path
        path = os.path.join(os.path.expanduser('~'), 'Downloads')
        # if user closes window
        # if event == '-URL-':
        #     yt = YouTube(values['-URL-'])
        #     newValues = 'Title\t: ' + yt.title + '\n' + 'Views\t: ' + str(yt.views) + '\n' + 'Durations\t: ' + str(round(yt.length/60, 2)) + '\n'
        #     window['-OUTPUT-'].update(newValues)
        if event == sg.WIN_CLOSED or None:
            break
        elif event == '-VIDEO-':
            yt = YouTube(values['-URL-'])
            newValues = 'Title\t: ' + yt.title + '\n' + 'Views\t: ' + str(yt.views) + '\n' + 'Durations\t: ' + str(round(yt.length/60, 2)) + '\n'
            window['-OUTPUT-'].update(newValues)
            ys = yt.streams.get_highest_resolution()
            ys.download(output_path=path)
        elif event == '-AUDIO-':
            yt = YouTube(values['-URL-'])
            newValues = 'Title\t: ' + yt.title + '\n' + 'Views\t: ' + str(yt.views) + '\n' + 'Durations\t: ' + str(round(yt.length/60, 2)) + '\n'
            window['-OUTPUT-'].update(newValues)
            ya = yt.streams.filter(only_audio=True)
            downFile = ya[0].download(output_path=path)
            base, ext = os.path.splitext(downFile)
            new_file = base + '.mp3'
            os.rename(downFile, new_file)
    window.close()

if __name__ == '__main__':
    main()