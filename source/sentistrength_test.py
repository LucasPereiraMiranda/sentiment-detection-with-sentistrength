# -*- coding: UTF-8 -*-

from sentistrength import PySentiStr


SENTISTRENGTH_DATA_PATH =  r'/home/lucas/dev/personal/sentiment-detection-with-sentistrength/source/sentistrength/SentiStrength_Data/'
SENTISTRENGTH_JAR_PATH = r'/home/lucas/dev/personal/sentiment-detection-with-sentistrength/source/sentistrength/SentiStrength.jar'

PHRASES_TO_TEST_PATH = r'/home/lucas/dev/personal/sentiment-detection-with-sentistrength/data/phrases-to-test.txt'



def main():
    sentistrength = PySentiStr()
    sentistrength.setSentiStrengthPath(SENTISTRENGTH_JAR_PATH)
    sentistrength.setSentiStrengthLanguageFolderPath(SENTISTRENGTH_DATA_PATH)
    
    with open(PHRASES_TO_TEST_PATH,'r') as file:
        file_lines = file.readlines()

    for line in file_lines:
        text = line.strip()
        result_scale = sentistrength.getSentiment(text,score ='scale')
        result_dual = sentistrength.getSentiment(text,score ='dual')
        result_trinary = sentistrength.getSentiment(text,score ='trinary')        
        print('text: {0}\nresult_scale: {1}\nresult_dual: {2}\nresult_trinary: {3}\n'
            .format(text,str(result_scale),str(result_dual),str(result_trinary)))

if __name__ == "__main__":
    main()
