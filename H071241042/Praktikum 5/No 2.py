def acronym(s):

    s = s.split()
    acronym = ''.join(huruf[0].upper() for huruf in s)
    print(acronym)

acronym("Negara Kesatuan Republik Indonesia")
acronym("Dewan Perwakilan Rakyat")