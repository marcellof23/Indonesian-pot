import PySimpleGUI as sg
import os
import base64


def main():
    OUTPUT_FILENAME = 'output.txt'

    folder = sg.popup_get_folder('Masukkin nama folder %s' % OUTPUT_FILENAME,
                                 title='Base64 Encoder')

    if not folder:
        sg.popup_cancel('Folder Invalid')
        return
    try:
        namesonly = [f for f in os.listdir(folder) if f.endswith(
            '.png') or f.endswith('.ico') or f.endswith('.gif')]
    except:
        sg.popup_cancel('Cancelled - No valid folder entered')
        return

    outfile = open(os.path.join(folder, OUTPUT_FILENAME), 'w')

    for i, file in enumerate(namesonly):
        contents = open(os.path.join(folder, file), 'rb').read()
        encoded = base64.b64encode(contents)
        outfile.write('\n{} = {}'.format(file[:file.index(".")], encoded))
        sg.OneLineProgressMeter('Base64 Encoding', i+1,
                                len(namesonly), key='-METER-')

    outfile.close()
    sg.popup('EZPZ!', 'Encoded %s files' % (i+1))


if __name__ == '__main__':
    main()
