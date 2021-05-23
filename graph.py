import networkx as nx
import matplotlib.pyplot as plt

def graph(list_nodes, mass):
    G = nx.DiGraph()
    plt.figure(figsize=(9,9))
    color_list = ['red']
    for i in range(12):
        color_list.append('yellow')

    for i in mass:
        G.add_edge(i[2], i[2])
    for i in range(len(list_nodes)):
        list_nodes[i] = tuple(list_nodes[i])
    G.add_edges_from(list_nodes)
    G = G.to_directed()

    pos={'Офис':(7.5,5),'Фучика':(8.7,5),'Седова':(10,6.5),'Новгородский':(9,1),'Поселковая':(10,1.5),'Бадаевский':(10.5,1),'Парнас':(10,16),'Моск. Шоссе':(12,0),'Лиговка':(9,8),'Гороховая':(7,8.5),'Васька':(6,10),'Кронштадт':(0,12),'Роменская':(8,8)}

    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G, pos=pos, node_color=color_list, with_labels=False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
    nx.draw_networkx_labels(G, pos, font_size=10)
    plt.show()

