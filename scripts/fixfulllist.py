'''
if VERSION < v"1.0"  
   @warn("the VoxForge scripts require version 1.0 and above")
end

function fixfulllist(in_fulllist, in_monophones0, out_fulllist)
  seen=Dict{String, Int32}()
  in_fulllist_arr=open(readlines, in_fulllist) # automatically closes file handle
  in_monophones0_arr=open(readlines, in_monophones0) # automatically closes file handle
  new_fulllist_arr=cat(in_fulllist_arr, in_monophones0_arr, dims=1)

  out_fulllist_fh=open(out_fulllist,"w")

  for phoneln=new_fulllist_arr
    phone=chomp(phoneln)
    if ! haskey(seen,phone) # remove duplicate monophone/triphone names
      seen[phone]=1
      write(out_fulllist_fh,phone * "\n")
    end
  end

  close(out_fulllist_fh)
end

# if called from command line
if length(ARGS) > 0 
  if ! isfile(ARGS[1])
    error("can't find fulllist file: $ARGS[1]")
  end
  if ! isfile(ARGS[2])
    error("can't find monophones0 file: $ARGS[2]")
  end
  if length(ARGS) > 3
    error("fixfulllist: too many arguments for call from command line\nusage: in_fulllist, in_monophones0, out_fulllist")
  end

  fixfulllist(ARGS[1], ARGS[2], ARGS[3])
end
'''

def fixfullList(in_fulllist, in_monophones0, out_fulllist):
    seen={}
    in_fullist_file = open(in_fulllist, "r")
    in_fulllist_arr = in_fullist_file.readlines()
    in_fullist_file.close()

    in_monophones0_file = open(in_monophones0, "r")
    in_monophones0_arr = in_monophones0_file.readlines()
    in_monophones0_file.close()

    new_fulllist_arr = in_fulllist_arr + in_monophones0_arr

    out_fulllist_file = open(out_fulllist,"w")

    for phoneln in new_fulllist_arr:
        phone = phoneln.strip()
        if phone not in seen:
            seen[phone] = True
            out_fulllist_file.write(phone + "\n")

    out_fulllist_file.close()

fixfullList("generated/fulllist0", "generated/monophones0", "generated/fulllist")