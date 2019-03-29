f=open('picgene.svg','w')
f.write('<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" \n"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')

f.write('<svg width="100%" height="100%" version="1.1"\nxmlns="http://www.w3.org/2000/svg">\n')

gene = raw_input('Add your gene here:')
gene=list(gene)

for i in range(len(gene)):
    if gene[i] == 'A':
        gene[i] = '0'
    elif gene[i] == 'T':
        gene[i] = '1'
    elif gene[i] == 'C':
        gene[i] = '2'
    else:
        gene[i] = '3'

clist=[]
for i in range(0,len(gene)-3,4):
    colornum=int(gene[i])*64+int(gene[i+1])*16+int(gene[i+2])*4+int(gene[i+3])
    clist = clist + [colornum]

clist = clist + [0,0,0]


for j in range(0,len(clist)-3,3):
    b = int(j/3)
    a = 20+b*2
    string='<rect x="'+str(a)+'" y="20" width="2" height="10"\nstyle="fill:rgb('+str(clist[j])+','+str(clist[j+1])+','+str(clist[j+2])+');stroke-width:0;\nstroke:rgb(0,0,0)"/>\n'
    f.write(string)

f.write('</svg>\n')
