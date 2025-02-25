import networkx as nx
from os import listdir
from music21 import *

G = nx.DiGraph();
#print(listdir("./"));

for file in listdir("./"):
    if file.endswith(".mxl"):
        b = converter.parse(file);
        # for note in b.parts[0].semiFlat.notesAndRests:
        #     print(note.fullName);
        melody = list(b.parts[0].semiFlat.notesAndRests);
        
        if (melody[0].isChord):
            G.add_node(melody[0].notes[-1].fullName);
        else:
            G.add_node(melody[0].fullName);
        
        for i in range(1,len(melody)):
            if (melody[i].isChord):
                melody[i] = melody[i].notes[-1];
                
            G.add_node(melody[i].fullName);
            if G.has_edge(melody[i].fullName, melody[i-1].fullName):
                G[melody[i].fullName][melody[i-1].fullName]['weight'] += 1;
            else:
                G.add_edge(melody[i].fullName, melody[i-1].fullName, weight=1);
            
            #print(melody[i].duration.type)
    #break;

print(G.number_of_nodes());
print(G.number_of_edges());

#nx.write_gexf(G, "sonatasBachViolin.gexf");