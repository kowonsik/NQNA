#-*- coding: utf-8 -*-

from nqna import *
from na_config import *
import sys

q_id={0:23, 1:10, 2:39, 3:44, 4:14, 5:33, 6:21, 7:66, 8:88, 9:11}
q_label={0:0, 1:4, 2:1, 3:2, 4:3, 5:4, 6:1, 7:2, 8:2, 9:1}
q_exemplar={0:23, 1:39, 2:44, 3:14, 4:33}

G_q = np.matrix([\
    [1, 0, 1, 0, 0],\
    [0, 1, 1, 0, 1],\
    [1, 1, 1, 1, 0],\
    [0, 0, 1, 1, 0],\
    [0, 1, 0, 0, 1]])


if __name__ == "__main__":

    """
    if len(sys.argv) > 1:
        graph_opt = sys.argv[1]
        print "sys.argv[%d],graph = %s" % (1, graph_opt)
        print "======================================="
        print "running news quatation network analysis....."
    else :
        print "Stop running, Please type graph option"
        print "======================================="
        print "python run.py all : all network showing"
        print "======================================="
        print "python run.py 1 : 1 group network showing"
        """
    graph_opt='all'
    # for fiding same label
    find_same_label(q_label,argv_print=False)

    # make graph
    #create_connect(q_id, q_exemplar, G_q, graph_opt, argv_print=False)
    create_connect(q_id, q_exemplar, G_q, graph_opt, argv_print=True)

    # excel id, label, exemplar, G_q(matrix) result
    write_excel_result(q_id, q_label, q_exemplar, G_q, RESULT_EXCEL, SHEET_COUNT, graph_opt, argv_print=False)
    

