# import fasttext

# Skipgram model
# model = fasttext.skipgram('data.txt', 'model')
# print(model.words) # list of words in dictionary
# print (model['no'])

# # CBOW model
# model = fasttext.cbow('data.txt', 'model')
# print(model.words) # list of words in dictionary
# print (model['lord'])


# import codecs
#
# # with codecs.open(filename, "r", "utf8")
#
# input = codecs.open("C:/Users/Pedro/Desktop/Suomi24-2015-05-25_JSON/dump33900-33999.json", "rb", encoding="utf-8")
# output = codecs.open("C:/Users/Pedro/Desktop/output.txt", "wb", encoding="utf-8")
#
# # Stream chunks of unicode data.
# with input, output:
#     while True:
#         # Read a chunk of data.
#         chunk = input.read(4096)
#         if not chunk:
#             break
#         # Remove vertical tabs.
#         chunk = chunk.replace(u"\u00e4", u"ä")
#         chunk = chunk.replace(u"\u00c4", u"Ä")
#         chunk = chunk.replace(u"\u00f6", u"ö")
#         chunk = chunk.replace(u"\u00d6", u"Ö")
#         chunk = chunk.replace(u"\u00e5", u"å")
#         chunk = chunk.replace(u"\u00c5", u"Å")
#         chunk = chunk.replace(u"\u00e1", u"á")
#         chunk = chunk.replace(u"\u00c1", u"Á")
#         # Write the chunk of data.
#         output.write(chunk)


# import io
# import os
#
# # Open both input and output streams.
# path = "C:/Users/Pedro/Desktop/Suomi24-2015-05-25_JSON/"
# # for filename in os.listdir(path):
# # input = io.open("C:/Users/Pedro/Desktop/Suomi24-2015-05-25_JSON/"+filename, "r", encoding="utf-8")
# # output = io.open("C:/Users/Pedro/Desktop/out/"+filename+".txt", "w", encoding="utf-8")
# input = io.open(path + "dump33900-33999.json", "r", encoding="utf-8")
# output = io.open("C:/Users/Pedro/Desktop/" + "out" + ".txt", "w",encoding="utf-8")
#
# # Stream chunks of unicode data.
# with input, output:
#     # while True:
#     # Read a chunk of data.
#     chunk = input.read()
#     # if not chunk:
#     #     break
#     # Remove vertical tabs.
#     chunk = chunk.replace("\\u00e4", u"\u00e4")
#     # chunk = chunk.replace("\\u00e4", "ä")
#     # chunk = chunk.replace("\\u00c4", "Ä")
#     # chunk = chunk.replace("\\u00f6", "ö")
#     # chunk = chunk.replace("\\u00d6", "Ö")
#     # chunk = chunk.replace("\\u00e5", "å")
#     # chunk = chunk.replace("\\u00c5", "Å")
#     # chunk = chunk.replace("\\u00e1", "á")
#     # chunk = chunk.replace("\\u00c1", "Á")
#     # chunk = chunk.replace("\\u00b4", "´")
#     # chunk = chunk.replace("\\u00a0", " ")
#     # chunk = chunk.replace("\\u00a7", "§")
#     # chunk = chunk.replace("\\u00b0", "°")
#     # chunk = chunk.replace("\\u00ed", "í")
#     # chunk = chunk.replace("\\u00e8", "é")
#     # chunk = chunk.replace("\\u00b7", "·")
#     # chunk = chunk.replace("\\u00fa", "ú")
#     # chunk = chunk.replace("\\u00a4", "¤")
#     # chunk = chunk.replace("\\u00a8", "¨")
#     # chunk = chunk.replace("\\u00fc", "ü")
#     # chunk = chunk.replace("\\u00d4", "Ó")
#     # chunk = chunk.replace("\\u00b2", "²")
#     # chunk = chunk.replace("\\u00b3", "³")
#     # chunk = chunk.replace("\\u00bd", "½")
#     # chunk = chunk.replace("\\u00e9", "é")
#     # chunk = chunk.replace("\\u00c9", "É")
#     # chunk = chunk.replace("\\u00dc", "Ü")
#     # chunk = chunk.replace("\\u00ae", "®")
#     # chunk = chunk.replace("\\u00a9", "©")
#     # chunk = chunk.replace("\\u00eb", "ë")
#     # chunk = chunk.replace("\\u00c2", "Â")
#     # chunk = chunk.replace("\\u00bc", "¼")
#     # chunk = chunk.replace("\\u00ad", "-")
#     # chunk = chunk.replace("\\u00bb", "»")
#     # chunk = chunk.replace("\\u00da", "Ú")
#     # chunk = chunk.replace("\\u00f3", "ó")
#     # chunk = chunk.replace("\\u00a1", "¡")
#     # chunk = chunk.replace("\\u00d1", "Ñ")
#     # chunk = chunk.replace("\\u00f1", "ñ")
#     # chunk = chunk.replace("\\u00d3", "Ó")
#     # chunk = chunk.replace("\\u00d7", "×")
#     #  Write the chunk of data.
#     output.write(chunk)


import json
# from pprint import pprint
import os
# import re

# path_input = "C:/Users/Pedro/Desktop/Suomi24-2015-05-25_JSON/"
# path_output = "C:/Users/Pedro/Desktop/out/"
# for filename in os.listdir(path_input):
#     with open(path_input + filename, "r", encoding="utf-8") as input:
#         with open(path_output + filename + ".txt", "w", encoding="utf-8") as output:
#             document = json.load(input)
#             json.dump(document, output, ensure_ascii=False)

path_input = "C:/Users/Pedro/Desktop/Suomi24-2015-05-25_JSON/"
# path_output = "C:/Users/Pedro/Desktop/out/"
for filename in os.listdir(path_input):
    with open(path_input + filename, "r", encoding="utf-8") as input:
        with open("C:/Users/Pedro/Desktop/input2.txt", "a", encoding="utf-8") as output:
            document = json.load(input)
            for line in document:
                json.dump(
                    # "Title: " +
                    line["title"]
                    # +
                    # "   Time: " +
                    # str(line["created_at"]) +
                    # "   Body: " +
                    # " " +
                    # line["body"].replace("<p>", " ").replace("</p>", " ")
                    , output, ensure_ascii=False)
                # pprint(line["title"])
                # pprint(line["body"])
                # pprint(line["created_at"])

# unicode_escape = re.compile(
#     r'(?<!\\)'
#     r'(?:\\u([dD][89abAB][a-fA-F0-9]{2})\\u([dD][c-fC-F][a-fA-F0-9]{2})'
#     r'|\\u([a-fA-F0-9]{4}))')
#
#
# def replace(m):
#     return chr(int(m.group(1), 16))
#
# path_input = "C:/Users/Pedro/Desktop/Suomi24-2015-05-25_JSON/"
# path_output = "C:/Users/Pedro/Desktop/out/"
# for filename in os.listdir(path_input):
#     with open(path_input + filename, "r", encoding="utf-8") as input:
#         with open(path_output + filename + ".txt", "w", encoding="utf-8") as output:
#             for line in input:
#                 output.write(unicode_escape.sub(replace, line))