import urllib2                                                                                                                                         
import re                                                                                                                                              
                                                                                                                                                       
def main():                                                                                                                                            
    #open url for reading webpage                                                                                                                      
    response = urllib2.urlopen('http://www.genome.jp/dbget-bin/get_linkdb?-t+2+genome:T01020')                                                         
    pathways = [] #list of pathway names                                                                                                               
    descriptionList = [] # descriptions of pathways                                                                                                    
    geneList = [] #genes in each pathway                                                                                                               
                                                                                                                                                       
    # get the name and description of each pathway and append to lists                                                                                 
    for line in response:                                                                                                                              
        if "/kegg-bin/show_pathway?" in line:                                                                                                          
            line = line.split("             ")                                                                                                         
            pathways.append(line[0][32:40])                                                                                                            
            description = line[1].split(" - ")                                                                                                         
            descriptionList.append(description[0])                                                                                                     
                                                                                                                                                       
    # open url page for each pathway. Then add genes for each pathway in a list of lists                                                               
    for path in pathways:                                                                                                                              
        tempGeneList = []                                                                                                                              
        site = urllib2.urlopen('http://rest.kegg.jp/get/'+path+"/")                                                                                    
        for line in site:                                                                                                                              
            if "TTHERM_" in line:                                                                                                                      
                line = line.split()                                                                                                                    
                if line[0] == "GENE":                                                                                                                  
                    tempGeneList.append(line[1])                                                                                                       
                else:                                                                                                                                  
                    tempGeneList.append(line[0])                                                                                                       
        geneList.append(tempGeneList)                                                                                                                  
                                                                                                                                                       
    for out in geneList:                                                                                                                               
        print out                                                                                                                                      
                                                                                                                                                       
    # write pathway, description, and genes to a tab delimited file                                                                                    
    f = open("pathways2.txt",'w')                                                                                                                      
    for p in range(len(pathways)):                                                                                                                     
        if len(geneList[p]) > 0:                                                                                                                       
            f.write(pathways[p] + "\t" + descriptionList[p] + "\t")                                                                                    
            for g in range(len(geneList[p])):                                                                                                          
                f.write(geneList[p][g] + "\t")                                                                                                         
            f.write("\n")                                                                                                                              
                                                                                                                                                       
                                                                                                                                                       
if __name__ == "__main__":                                                                                                                             
    main()     
