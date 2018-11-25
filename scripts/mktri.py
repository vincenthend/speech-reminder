'''
function mktrihed(monophones, triphones, mktri) 
  monophones_arr=open(readlines, monophones)  # automatically closes file handle

  hed=open(mktri, "w") 
  write(hed, "CL $triphones\n")
  for phoneln=monophones_arr
    phone=chomp(phoneln)
    if length(phone)>0
      write(hed,"TI T_$phone {(*-$phone+*,$phone+*,*-$phone).transP}\n")
    end
  end
  close(hed)
end

# if called from command line
if length(ARGS) > 0 
  if ! isfile(ARGS[1])
    error("can't find monophones file: $ARGS[1]")
  end
  if ! isfile(ARGS[2])
    error("can't find triphones file: $ARGS[2]")
  end
  if length(ARGS) > 3 
    error("prompts2list: too many arguments for call from command line")
  end

  mktrihed(ARGS[1], ARGS[2], ARGS[3])
end
'''

def mktrihed(monophones, triphones, mktri):
    monophones_files = open(monophones, "r")
    monophones_arr = monophones_files.readlines()
    monophones_files.close()

    trihed_file = open(mktri, "w")
    trihed_file.write("CL "+triphones+"\n")
    for phoneln in monophones_arr:
        phone = phoneln.strip()
        if len(phone)>0:
            trihed_file.write("TI T_%s {(*-%s+*,%s+*,*-%s).transP}\n" % (phone, phone, phone, phone))
    trihed_file.close()

mktrihed("generated/monophones1", "generated/triphones1", "generated/mktri.hed")