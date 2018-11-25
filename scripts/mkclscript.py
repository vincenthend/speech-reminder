def mkclscript(monophones0, tree_hed, old_tree, folder):
  tree = open(old_tree,"r")
  tree_arr = tree.readlines()
  tree.close()

  hmmlist = open(tree_hed,"w")
  hmmlist.writelines(tree_arr)

  monophones0_file = open(monophones0, "r")
  monophones0_arr = monophones0_file.readlines()
  monophones0_file.close()

  for i in range(2,5):
    for phoneln in monophones0_arr:
      phone = phoneln.strip()
      hmmlist.write("TB 350 \"ST_"+phone+"_"+str(i)+"_\" {(\""+phone+"\",\"*-"+phone+"+*\",\""+phone+"+*\",\"*-"+phone+"\").state["+str(i)+"]}\n")

  hmmlist.write("\n") 
  hmmlist.write("TR 1\n")
  hmmlist.write("\n") 
  hmmlist.write("AU \""+folder+"/fulllist\" \n")
  hmmlist.write("CO \""+folder+"/tiedlist\" \n")
  hmmlist.write("\n") 
  hmmlist.write("ST \""+folder+"/trees\" \n")

  hmmlist.close()

mkclscript("generated/monophones0", "generated/tree.hed", "train/tree.hed", "generated")