import json
from gingerit.gingerit import GingerIt

class Text:
    def __init__(self, input_text):
        self.text = input_text 
        self.err_tot = 0
        self.err_gram = 0
        self.err_mec = 0
    
    def calc_err_tot(self):
        self.err_tot = self.err_gram + self.err_mec

    def set_err_gram(self,val):
        self.err_gram = val
        self.calc_err_tot()
    
    def set_err_mec(self,val):
        self.err_mec = val
        self.calc_err_tot()

class Analyze:
    def __init__(self) -> None:
        self.my_mistakes = []
        self.my_corrections = []
        self.start_positions = []
        self.end_positions = []
    
    def start(self, text):
        pass

class AnalyzeGrammar(Analyze):
    # def start(self, text):
    #     # text = 'Donald Trump lose the presendential election, Joe Biden is the new president of Amrica.'
    #     # tool = language_tool_python.LanguageToolPublicAPI('en-US')
    #     tool = language_tool_python.LanguageTool('en-US')
    #     matches = tool.check(text)
    #     ret = []
        
    #     for rules in matches:
    #         if len(rules.replacements)>0:
    #             self.start_positions.append(rules.offset)
    #             self.end_positions.append(rules.errorLength+rules.offset)
    #             self.my_mistakes.append(text[rules.offset:rules.errorLength+rules.offset])
    #             self.my_corrections.append(rules.replacements[0])

    #     ret = {
    #         "mistakes":self.my_mistakes,
    #         "corrections":self.my_corrections,
    #         "start_posititons":self.start_positions,
    #         "end_position":self.end_positions
    #     }

    #     return ret, len(matches)
        
    def start(self, text):
        ret = []
        result = GingerIt().parse(text)
        for correction in result.get('corrections'):
            if len(result.get('corrections')) > 0:
                self.start_positions.append(correction.get('start'))
                self.end_positions.append(correction.get('start') + len(correction.get('text')) - 1)
                self.my_mistakes.append(correction.get('text'))
                self.my_corrections.append(correction.get('correct'))
        
        ret = {
            "mistakes":self.my_mistakes,
            "corrections":self.my_corrections,
            "start_posititons":self.start_positions,
            "end_position":self.end_positions
        }
        return len(result.get('corrections')), ret

class AnalyzeMec(Analyze):
    def start(self, text):
        return super().start(text)
    
# def analyze_mec(text):
#         from punctuator import Punctuator
#         p = Punctuator('model.pcl')
#         x = p.punctuate(text)
#         y = 0

#         # for i in range(0, len(x)):
#         #     if(text[i] == ' ' and (x[i] == '!' or x[i] == '.' or x[i] == ',' or x[i] == '?')):
#         #         continue
#         #     elif(x[i] != text[i]):
#         #         y += 1
#         return x

# instance = Analyze()
# print(AnalyzeGrammar.start("Heloo Wrld"))
