def plot_from_file(substrate, width, height):
    data={}
    with open(substrate+'_before.w','r') as w,open(substrate+'_before.l','r') as l,open(substrate+'_results.txt') as txt:
        for line in txt:
            topo=line.strip()
            if topo not in data.keys():
                data[topo]=[[float(w.readline().strip())],[float(l.readline().strip())],1]
            else:
                try:
                    data[topo][0].append(float(w.readline().strip()))
                    data[topo][1].append(float(l.readline().strip()))
                    data[topo][2]+=1
                except ValueError:
                    pass
    subplotnum=0
    #init a grid; a column with height = number of subplots
    G = gs.GridSpec(len(data.keys()),1)
    #make figure more column-shaped
    figarea = plt.rcParams["figure.figsize"]
    figarea[0]=width
    figarea[1]=height
    #not sure if this is working but it's supposed to decrease tick size
    plt.rcParams["xtick.minor.size"]=.5
    plt.rcParams["ytick.minor.size"]=.5
    for topo in data.keys():
        fig=plt.subplot(G[subplotnum])
        subplotnum+=1
        #normed = false ; colorbar shows "amount of transitions per square", not percentages
        plt.hist2d(data[topo][0],data[topo][1], bins=20,normed=False, alpha=.75)
        plt.xlabel('writhe average: '+str(np.mean(data[topo][0])))
        #plt.ylabel('sample size: '+str(len(products[topo])))
        plt.title('Transition '+substrate+' to '+topo+' Total: '+str(data[topo][2]))
        plt.colorbar(spacing='proportional')
        #tight_layout ensures no clipping of labels
        plt.tight_layout()
    plt.savefig('3_1_BFACFlw_trans_freq.png')
    plt.show()

