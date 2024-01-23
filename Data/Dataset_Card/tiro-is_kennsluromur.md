
# KENNSLURÓMUR - ICELANDIC LECTURES
### [Icelandic]

Kennslurómur - Íslenskir fyrirlestrar er safn af hljóðskrám og samsvarandi texta úr kennslufyrirlestrum sem teknir voru upp í áföngum í Háskólanum í Reykjavík og Háskóla Íslands. Þetta safn má nota við þjálfun talgreina.

Fyrirlesararnir gáfu upptökurnar sínar sem síðan voru talgreindar með talgreini, næst  var frálagið lesið og leiðrétt af hópi sumarnema og að lokum var allur texti yfirfarinn af prófarkalesara. 

Í þessu safni eru 51 klukkustund af hljóðskrám sem dreifast á 171 fyrirlestur frá 11 fyrirlesurum.

### [English]

Kennslurómur - Icelandic Lectures is a collection of audio recordings and their corresponding segmented transcripts from class lectures recorded at Reykjavik University and the University of Iceland. This material was compiled for the training of speech recognition models.

The lectures were donated by each lecturer, then transcribed with an Icelandic speech recognizer, then manually corrected by human transcribers and finally verified by a proofreader. 

This release contains 51 hours divided between 171 lectures from 11 lecturers. 

## LECTURE TOPICS
The topic of the lextures cover a diverse range of university level subjects. 
```
Linguistics         	   15 lectures	1 speaker	7,12 hours
Computer science	       33 lectures	3 speakers	15,3 hours
Labour market economics	   13 lectures	1 speaker	1,91 hours
Engineering                64 lectures	3 speakers	11,3 hours
Legal studies	           25 lectures	2 speakers	7,52 hours
Business intelligence	    1 lecture	1 speaker	19,2 minutes
Psychology	               10 lectures	1 speaker	3,03 hours
Sports science             10 lectures	1 speaker	4,79 hours
```

## STRUCTURE

    SPEAKERS.tsv                        -  Lists the speakers (lecturers) and their IDs.
    LECTURES.tsv                        -  Lists all lectures. See header for the format.
    DOCS/
        transcription_guidelines_is.txt -  Transcription guidelines in Icelandic.
    LICENSE.txt                         -  Description of the license.
    prerp_for_training.py               -  An example data preparation script for KALDI.
    <SPK-ID>/                           -  A directory per speaker.
        <LECTURE-ID>.wav                -  Audio recording of the entire lecture.
        <LECTURE-ID>.txt                -  Transcript of the entire lecture in 1 to 
                                           40 second segments. Tab separated list with the
                                           fields: segment ID, start time in milliseconds, 
                                           end time in milliseconds and utterance text.


## Alignment and segmentation
The segments are mostly split on sentence boundaries. Each segment ranges from a few seconds to roughly 40 seconds in duration. The recordings and transcripts were automatically aligned using either [Montreal Forced Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) or the aligner [Gentle](https://github.com/lowerquality/gentle). The alignment quality was tested by training an acoustic model in Kaldi and rejected segments due to alignment issues. Recordings with an abnormally high number of faulty segments were manually aligned. This means that there are likely still some imperfectly aligned segments, but due to resource constraints, they were not manually checked and verified. 


## Training, development and testing sets
Every segment has been marked as either train, dev or eval. This can be seen in the \<SPK-ID\>/\<LECTURE-ID\>.txt files. There are a few speakers in this dataset creating training sets without overlap of speakers is not possible without holding out a large portion of the data. Therefore, it was decided to randomly assign each speaker's segments proportionally 80/10/10 (train, dev, eval) based on the duration of each segment.


## FORMAT
    Sampling rate     16000 Hz
    Audio format      16 bit PCM RIFF WAVE
    Language          Icelandic
    Type of speech    Single speaker spontaneous and scripted speech with minimal
                      backspeech.
    Media type        Recorded university lectures, a mixture of prerecorded 
                      classes and in-class recordings.


## SPECIAL ANNOTATIONS

Three types of special annotations are found the transcripts:


    [UNK]           Unintelligible, spoken background noise

    [HIK: <stubs>]  Hesitation, where <stubs> can be a comma separated list
                    of false start (often partial) words.

    [<IPA sym>]     Standalone IPA phones are transcribed in brackets which
                    only appear in "Icelandic linguistics" lectures.
                    E.g. "Þannig fáum við eins og raddað b, [p] [p] [p] 
                    „bera bera“.".


## LICENSE

The audio recordings (.wav files) are attributed to the corresponding lecturer
in the file `SPEAKERS.tsv`. Everything else is attributed to 
[Tiro ehf](https://tiro.is).

Published with a CC BY 4.0 license. You are free to copy and redistribute the 
material in any medium or format, remix, transform and build upon the material 
for any purpose, even commercially under the following terms: You must give 
appropriate credit, provide a link to the license, and indicate if changes were 
made. You may do so in any reasonable manner, but not in any way that suggests 
the licensor endorses you or your use. 

Link to the license: https://creativecommons.org/licenses/by/4.0/


## ACKNOWLEDGMENTS

This project was funded by the Language Technology Programme for Icelandic
2019-2023. The programme, which is managed and coordinated by Almannarómur, is
funded by the Icelandic Ministry of Education, Science and Culture.

