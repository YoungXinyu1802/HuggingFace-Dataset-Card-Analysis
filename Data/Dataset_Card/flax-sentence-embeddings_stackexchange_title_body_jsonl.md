jsonl.gz format from https://huggingface.co/datasets/flax-sentence-embeddings/stackexchange_xml

Each line contains a dict in the format: \
{"text": ["title", "body"], "tags": ["tag1", "tag2"]}

The following parameters have been used for filtering: \
min_title_len = 20 \
min_body_len = 20 \
max_body_len = 4096 \
min_score = 0  

If a stackexchange contained less than 10k questions (after filtering), it is written to the `small_stackexchanges.jsonl.gz` file.

This is a dump of the files from https://archive.org/details/stackexchange

downloaded via torrent on 2021-07-01.

Publication date 2021-06-07  \
Usage Attribution-ShareAlike 4.0 International Creative Commons License by sa  \


Please see the license information at: https://archive.org/details/stackexchange



## Examples (lines) per file:

stackoverflow.com-Posts.jsonl.gz: 18,562,443\
math.stackexchange.com.jsonl.gz: 1,338,443\
small_stackexchanges.jsonl.gz: 448,146\
superuser.com.jsonl.gz: 435,463\
askubuntu.com.jsonl.gz: 347,925\
serverfault.com.jsonl.gz: 270,904\
tex.stackexchange.com.jsonl.gz: 202,954\
unix.stackexchange.com.jsonl.gz: 185,997\
stats.stackexchange.com.jsonl.gz: 173,466\
physics.stackexchange.com.jsonl.gz: 173,307\
electronics.stackexchange.com.jsonl.gz: 143,582\
gis.stackexchange.com.jsonl.gz: 131,000\
mathoverflow.net.jsonl.gz: 120,851\
apple.stackexchange.com.jsonl.gz: 110,622\
english.stackexchange.com.jsonl.gz: 109,522\
salesforce.stackexchange.com.jsonl.gz: 105,260\
wordpress.stackexchange.com.jsonl.gz: 100,474\
magento.stackexchange.com.jsonl.gz: 99991\
sharepoint.stackexchange.com.jsonl.gz: 94011\
gaming.stackexchange.com.jsonl.gz: 88912\
meta.stackexchange.com.jsonl.gz: 83510\
ell.stackexchange.com.jsonl.gz: 83271\
dba.stackexchange.com.jsonl.gz: 81871\
blender.stackexchange.com.jsonl.gz: 80766\
drupal.stackexchange.com.jsonl.gz: 79717\
mathematica.stackexchange.com.jsonl.gz: 73131\
scifi.stackexchange.com.jsonl.gz: 61528\
diy.stackexchange.com.jsonl.gz: 60083\
security.stackexchange.com.jsonl.gz: 58000\
softwareengineering.stackexchange.com.jsonl.gz: 53942\
android.stackexchange.com.jsonl.gz: 51608\
gamedev.stackexchange.com.jsonl.gz: 46485\
codereview.stackexchange.com.jsonl.gz: 45765\
rpg.stackexchange.com.jsonl.gz: 42303\
travel.stackexchange.com.jsonl.gz: 41227\
cs.stackexchange.com.jsonl.gz: 38314\
meta.stackoverflow.com.jsonl.gz: 36456\
webmasters.stackexchange.com.jsonl.gz: 34559\
chemistry.stackexchange.com.jsonl.gz: 34506\
academia.stackexchange.com.jsonl.gz: 34331\
ethereum.stackexchange.com.jsonl.gz: 32760\
judaism.stackexchange.com.jsonl.gz: 32028\
money.stackexchange.com.jsonl.gz: 32021\
raspberrypi.stackexchange.com.jsonl.gz: 30625\
graphicdesign.stackexchange.com.jsonl.gz: 30233\
webapps.stackexchange.com.jsonl.gz: 29697\
ux.stackexchange.com.jsonl.gz: 29403\
datascience.stackexchange.com.jsonl.gz: 27397\
worldbuilding.stackexchange.com.jsonl.gz: 26763\
bitcoin.stackexchange.com.jsonl.gz: 25374\
biology.stackexchange.com.jsonl.gz: 24447\
workplace.stackexchange.com.jsonl.gz: 24189\
photo.stackexchange.com.jsonl.gz: 23753\
cooking.stackexchange.com.jsonl.gz: 23705\
crypto.stackexchange.com.jsonl.gz: 23231\
mechanics.stackexchange.com.jsonl.gz: 22868\
japanese.stackexchange.com.jsonl.gz: 22056\
dsp.stackexchange.com.jsonl.gz: 21252\
emacs.stackexchange.com.jsonl.gz: 21055\
music.stackexchange.com.jsonl.gz: 20636\
movies.stackexchange.com.jsonl.gz: 20181\
softwarerecs.stackexchange.com.jsonl.gz: 20142\
aviation.stackexchange.com.jsonl.gz: 20139\
arduino.stackexchange.com.jsonl.gz: 19553\
law.stackexchange.com.jsonl.gz: 17941\
puzzling.stackexchange.com.jsonl.gz: 17851\
quant.stackexchange.com.jsonl.gz: 17261\
rus.stackexchange.com.jsonl.gz: 16871\
bicycles.stackexchange.com.jsonl.gz: 16353\
space.stackexchange.com.jsonl.gz: 15142\
gardening.stackexchange.com.jsonl.gz: 15136\
philosophy.stackexchange.com.jsonl.gz: 14829\
german.stackexchange.com.jsonl.gz: 13950\
networkengineering.stackexchange.com.jsonl.gz: 13454\
hinduism.stackexchange.com.jsonl.gz: 13450\
craftcms.stackexchange.com.jsonl.gz: 12574\
civicrm.stackexchange.com.jsonl.gz: 12543\
boardgames.stackexchange.com.jsonl.gz: 12149\
christianity.stackexchange.com.jsonl.gz: 12108\
history.stackexchange.com.jsonl.gz: 12021\
politics.stackexchange.com.jsonl.gz: 11894\
expressionengine.stackexchange.com.jsonl.gz: 11866\
islam.stackexchange.com.jsonl.gz: 11853\
anime.stackexchange.com.jsonl.gz: 11444\
economics.stackexchange.com.jsonl.gz: 11115\
french.stackexchange.com.jsonl.gz: 10794\
engineering.stackexchange.com.jsonl.gz: 10753\
cstheory.stackexchange.com.jsonl.gz: 10642\
vi.stackexchange.com.jsonl.gz: 10551\
astronomy.stackexchange.com.jsonl.gz: 10462\
writers.stackexchange.com.jsonl.gz: 10157\
skeptics.stackexchange.com.jsonl.gz: 10009\
**Total: 25,333,327**
