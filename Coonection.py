from py2neo import Graph
from nlp_part import processData
from ml_model import mlPreddict

def makeGraph(sentence):
    graph = Graph("http://localhost:7474", auth=('neo4j', '123'))

    

    label_1, relation, label_2 = processData(sentence)

    type1 = mlPreddict(label_1)
    type2 = mlPreddict(label_2)

    query = """
    MERGE (p:%s{label:'%s'})
    MERGE (a:%s{label:'%s'})
    MERGE (p)-[:%s]->(a)
    """%(type1, label_1, type2, label_2, relation)

    graph.run(query)