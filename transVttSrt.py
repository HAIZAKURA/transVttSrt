# -*- coding: utf-8 -*-

import os
import re

path = os.path.split(os.path.realpath(__file__))

def getFileName(key):
    FileName = []
    for getFile in os.listdir(path[0]):
        if key == 'A':
            if os.path.splitext(getFile)[1] == '.vtt':
                # print(getFile)
                FileName.append(os.path.splitext(getFile)[0])
        elif key == 'B':
            if os.path.splitext(getFile)[1] == '.srt':
                # print(getFile)
                FileName.append(os.path.splitext(getFile)[0])
    return FileName

def vtt2srt(inFileName):
    subNo = 1
    outFileName = inFileName + '.srt'
    inFileName = inFileName + '.vtt'
    with open(inFileName, 'r', encoding='utf-8') as procFile:
        outFile = open(outFileName, 'w+', encoding='utf-8')
        for lineIndex, lineContent in enumerate(procFile.readlines()):
            if lineIndex > 0 and len(lineContent.strip()) != 0:
                if re.match('(\d{2}:\d{2}:\d{2}).(\d{3})', lineContent):
                    outFile.write('\n' + str(subNo) + '\n')
                    lineContent = re.sub('(\d{2}:\d{2}:\d{2}).(\d{3})', lambda m: m.group(1) + ',' + m.group(2), lineContent)
                    subNo += 1
                outFile.write(lineContent)
    outFile.close()
    print('[' + inFileName + '] transform completed!')

def srt2vtt(inFileName):
    subNo = 1
    outFileName = inFileName + '.vtt'
    inFileName = inFileName + '.srt'
    with open(inFileName, 'r', encoding='utf-8') as procFile:
        outFile = open(outFileName, 'w+', encoding='utf-8')
        outFile.write('WEBVTT\n')
        for lineContent in procFile.readlines():
            if lineContent.strip() == str(subNo):
                subNo += 1
                pass
            else:
                if re.match('(\d{2}:\d{2}:\d{2}),(\d{3})', lineContent):
                    lineContent = re.sub('(\d{2}:\d{2}:\d{2}),(\d{3})', lambda m: m.group(1) + '.' + m.group(2), lineContent)
                outFile.write(lineContent)
    outFile.close()
    print('[' + inFileName + '] transform completed!')

def main():
    key = input('A for vtt->srt || B for srt->vtt\n')
    print()
    if key == 'A':
        allFileName = getFileName(key)
        if allFileName == []:
            print('There are no vtt files here.')
        else:
            for fileName in allFileName:
                vtt2srt(fileName)
    elif key == 'B':
        allFileName = getFileName(key)
        if allFileName == []:
            print('There are no srt files here.')
        else:
            for fileName in allFileName:
                srt2vtt(fileName)
    else:
        print('Wrong method. Please input again.')
        main()

if __name__ == '__main__':
    print('\nCurrent directory: ' + path[0])
    print('\nPlease input the method of subtitle transforming.')
    main()
    input("\nMission Completed.")
