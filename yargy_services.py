from yargy.tokenizer import MorphTokenizer
from ipymarkup import show_span_ascii_markup
from yargy import rule, Parser
import services as sv

TOKENIZER = MorphTokenizer()

SERVICES = sv.all_services

line = 'АРХАНГЕЛЬСКАЯ ГОРОДСКАЯ ПОЛИКЛИНИКА №1, ГБУЗ АО (г. Архангельск, пр.Троицкий, 99), роды, скорая'
Measure = rule(SERVICES)

parser = Parser(Measure)

# matches = list(parser. findall(line))
# spans = [_.span for _ in matches]
# print(spans)
# aaa = spans[0]
# print(aaa)
# print(line[83:87])
# # print(matches[0], type(matches[0]))
# show_span_ascii_markup(line, spans)

def findServices(text):
    services = []
    servicesStr = ""
    for match in parser.findall(text):
        for x in match.tokens:
            value = x.value
            services.append(value)
    for _ in services:
        servicesStr += str(_) + " "
    return servicesStr


#print(findServices("АРХАНГЕЛЬСКАЯ ГОРОДСКАЯ ПОЛИКЛИНИКА №1, ГБУЗ АО (г. Архангельск, пр.Троицкий, 99), роды, скорая"))

#def findServices():

# addres = []
#     addrStr = ''
#     morph_vocab = MorphVocab()
#     addr_extractor = AddrExtractor(morph_vocab)
#     result = addr_extractor.find(text)
#     for addr in result.fact.parts:
#         addres.append(addr.type)
#         addres.append(addr.value)
#     for _ in addres:
#         addrStr += str(_) + " "
#     return addrStr