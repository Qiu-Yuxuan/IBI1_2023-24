import time
# record the start time of DOM
start_time1 = time.time()
import xml.dom.minidom
dom_tree = xml.dom.minidom.parse('d:/文档/大一下/IBI1/IBI1_2023-24/Practical14/go_obo.xml') #open the xml file
root = dom_tree.documentElement
terms = root.getElementsByTagName('term') #get all root
molecular_function_count = 0 #creat the counter
biological_process_count = 0
cellular_component_count = 0
for term in terms:
    namespace = term.getElementsByTagName('namespace')[0].firstChild.data
    # count number of three ontologies
    if namespace == 'molecular_function':
        molecular_function_count += 1
    elif namespace == 'biological_process':
        biological_process_count += 1
    elif namespace == 'cellular_component':
        cellular_component_count += 1

# print the result
print("Molecular Function:", molecular_function_count)
print("Biological Process:", biological_process_count)
print("Cellular Component:", cellular_component_count)
# record the end time of DOM
end_time1 = time.time()
execution_time1 = end_time1 - start_time1
start_time2 = time.time()
#code of SAX
import xml.sax
class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.namespace = ""
        self.molecular_function_count = 0
        self.biological_process_count = 0
        self.cellular_component_count = 0

    def startElement(self, name, attrs):
        if name == "namespace":
            self.namespace = ""
    
    def characters(self, content):
        self.namespace += content
    
    def endElement(self, name):
        if name == "namespace":
            if self.namespace == "molecular_function":
                self.molecular_function_count += 1
            elif self.namespace == "biological_process":
                self.biological_process_count += 1
            elif self.namespace == "cellular_component":
                self.cellular_component_count += 1
parser = xml.sax.make_parser()# create a sax resolver
parser.setFeature(xml.sax.handler.feature_namespaces, 0)#Turn off namespace processing
handler = MyHandler()# create a ContentHandler
# Assign the ContentHandler to the parser
parser.setContentHandler(handler)
# Parse xxl files
parser.parse("d:/文档/大一下/IBI1/IBI1_2023-24/Practical14/go_obo.xml")
# print the number of terms
print("Molecular Function:", handler.molecular_function_count)
print("Biological Process:", handler.biological_process_count)
print("Cellular Component:", handler.cellular_component_count)
end_time2 = time.time()
execution_time2 = end_time2 - start_time2
import matplotlib.pyplot as plt
# draw bar chart
categories = ['Molecular Function', 'Biological Process', 'Cellular Component']
counts = [molecular_function_count, biological_process_count, cellular_component_count]
plt.bar(categories, counts)
plt.xlabel('Ontology')
plt.ylabel('Count')
plt.title('GO Term Counts in Different Ontologies')
plt.show()
print("DOM Time:", execution_time1, "seconds",'SAX Time:',execution_time2)